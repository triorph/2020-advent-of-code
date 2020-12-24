import tqdm

MY_INPUT = "215694783"


class WeirdCupGame:
    def __init__(self, input):
        self._input = input
        self.reset_for_input()

    def reset_for_input(self):
        self._cups = [int(i) for i in self._input]
        self._max_val = max(self._cups)
        self._current_cup = self._cups[0]
        self._next_cups = {}
        for i in range(len(self._cups) - 1):
            self._next_cups[self._cups[i]] = self._cups[i + 1]

        self._next_cups[self._cups[-1]] = self._cups[0]

    def _find_next_target(self, cups_to_withhold):
        val = None
        for i in range(4):
            test_val = self._current_cup - i - 1
            if test_val > 0 and test_val not in cups_to_withhold:
                val = self._current_cup - i - 1
                break
        if val is None:
            val = self._max_val
            while val in cups_to_withhold:
                val -= 1
        return val

    def do_one_iteration(self):
        cups_to_withold = [self._next_cups[self._current_cup]]
        for _ in range(2):
            cups_to_withold.append(self._next_cups[cups_to_withold[-1]])
        target = self._find_next_target(cups_to_withold)
        targets_next = self._next_cups[target]
        self._next_cups[target] = cups_to_withold[0]
        self._next_cups[self._current_cup] = self._next_cups[cups_to_withold[-1]]
        self._next_cups[cups_to_withold[-1]] = targets_next
        self._current_cup = self._next_cups[self._current_cup]

    def _cups_printed(self, starting_cup, max_size):
        ret = ""
        current_char = self._next_cups[starting_cup]
        for i in range(max_size):
            ret = ret + str(current_char)
            current_char = self._next_cups[current_char]
        return ret

    def day_a(self):
        for i in range(100):
            self.do_one_iteration()

        return self._cups_printed(starting_cup=1, max_size=8)

    def _expand_maxval(self, maxval):
        self._max_val = maxval
        for j in range(len(self._cups) + 1, self._max_val):
            self._next_cups[j] = j + 1
        self._next_cups[self._cups[-1]] = len(self._cups) + 1
        self._next_cups[self._max_val] = self._cups[0]

    def day_b(self):
        self.reset_for_input()
        self._expand_maxval(1 * 1000 * 1000)
        for _ in tqdm.tqdm(range(10 * 1000 * 1000)):
            self.do_one_iteration()

        first = self._next_cups[1]
        second = self._next_cups[first]
        print("got day_b:", first, second)
        return first * second


if __name__ == "__main__":
    # d23test = WeirdCupGame("389125467")
    # test_day_b = d23test.day_b()
    # print("d23testb:", test_day_b)
    # assert test_day_b == 934001*159792

    d23 = WeirdCupGame(MY_INPUT)
    print("d23a:", d23.day_a())
    print("d23b:", d23.day_b())
