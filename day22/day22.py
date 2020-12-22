from copy import copy


class RepeatedGameError(Exception):
    pass


class CardGameDay22:
    def __init__(self, filename=None, p1_cards=[], p2_cards=[]):
        self._p1_cards = copy(p1_cards)
        self._p2_cards = copy(p2_cards)
        self._all_hashes = []
        if filename:
            self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        self._p1_cards = []
        for line in lines[1:]:
            try:
                self._p1_cards.append(int(line))
            except ValueError:
                break
        self._p2_cards = []
        for line in lines[3 + len(self._p1_cards) :]:
            try:
                self._p2_cards.append(int(line))
            except ValueError:
                break

    def _pop_cards_if_needed(self, p1_card, p2_card):
        if p1_card is None:
            p1_card = self._p1_cards.pop(0)
        if p2_card is None:
            p2_card = self._p2_cards.pop(0)
        return p1_card, p2_card

    def _current_hash(self):
        cards_str = "-".join(
            [
                ",".join([str(card) for card in self._p1_cards]),
                ",".join([str(card) for card in self._p2_cards]),
            ]
        )
        return hash(cards_str)

    def _player_1_wins(self, p1_card=None, p2_card=None):
        p1_card, p2_card = self._pop_cards_if_needed(p1_card, p2_card)
        self._p1_cards.extend([p1_card, p2_card])

    def _player_2_wins(self, p1_card=None, p2_card=None):
        p1_card, p2_card = self._pop_cards_if_needed(p1_card, p2_card)
        self._p2_cards.extend([p2_card, p1_card])

    def _do_recursive_game(self, p1_card, p2_card):
        new_game = CardGameDay22(
            p1_cards=self._p1_cards[:p1_card], p2_cards=self._p2_cards[:p2_card]
        )
        if new_game.do_all_rounds_b():
            self._player_1_wins(p1_card, p2_card)
        else:
            self._player_2_wins(p1_card, p2_card)

    def _latest_round_already_happened(self):
        round_hash = self._current_hash()
        return round_hash in self._all_hashes

    def _add_hash(self):
        self._all_hashes.append(self._current_hash())

    def _do_one_round_b(self):
        if self._latest_round_already_happened():
            raise RepeatedGameError("This round already happened")
        else:
            self._add_hash()
            p1_card = self._p1_cards.pop(0)
            p2_card = self._p2_cards.pop(0)
            if len(self._p1_cards) >= p1_card and len(self._p2_cards) >= p2_card:
                self._do_recursive_game(p1_card, p2_card)
            elif p1_card > p2_card:
                self._player_1_wins(p1_card, p2_card)
            else:  # p2_card > p1_card
                self._player_2_wins(p1_card, p2_card)

    def do_all_rounds_b(self):
        """Do all rounds for day b, then return if player 1 wins"""
        try:
            while self._rounds_to_do():
                self._do_one_round_b()
            return len(self._p1_cards) > 0
        except RepeatedGameError:
            return True

    def _do_one_round_a(self):
        p1_card = self._p1_cards.pop(0)
        p2_card = self._p2_cards.pop(0)
        if p1_card > p2_card:
            self._p1_cards.extend([p1_card, p2_card])
        else:  # no copies so means p2_card > p1_card
            self._p2_cards.extend([p2_card, p1_card])

    def _rounds_to_do(self):
        return len(self._p1_cards) > 0 and len(self._p2_cards) > 0

    def do_all_rounds_a(self):
        """Do all rounds and then return if player 1 wins"""
        while self._rounds_to_do():
            self._do_one_round_a()
        return len(self._p1_cards) > 0

    def _calculate_score(self, cards):
        ret = 0
        for i, card in enumerate(cards[::-1]):
            ret += (i + 1) * card
        return ret

    def day_a(self):
        p1_winner = self.do_all_rounds_a()
        if p1_winner:
            cards = self._p1_cards
        else:
            cards = self._p2_cards
        return self._calculate_score(cards)

    def day_b(self):
        p1_winner = self.do_all_rounds_b()
        if p1_winner:
            cards = self._p1_cards
        else:
            cards = self._p2_cards
        return self._calculate_score(cards)


if __name__ == "__main__":
    d22a = CardGameDay22("input_data.txt")
    print("d22a:", d22a.day_a())
    d22b = CardGameDay22("input_data.txt")
    print("d22b:", d22b.day_b())
