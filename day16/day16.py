from copy import deepcopy


class TicketCheckerDay16:
    def __init__(self, filename):
        self._raw_data = []
        self._rules = {}
        self._my_ticket = []
        self._other_tickets = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        self._build_rules(lines[:20])

        self._my_ticket = [int(number) for number in lines[22].split(",")]
        self._build_other_tickets(lines[25:])

    def _build_rules(self, lines):
        for line in lines:
            rule_name, rule_data = line.split(":")

            vals = [
                [int(val) for val in rule.strip().split("-")]
                for rule in rule_data.strip().split(" or ")
            ]
            self._rules[rule_name] = vals

    def _build_other_tickets(self, lines):
        for line in lines:
            self._other_tickets.append([int(val) for val in line.split(",")])

    def _validate_rule(self, rule, val):
        for lower, upper in self._rules[rule]:
            if val >= lower and val <= upper:
                return True
        return False

    def validate_val(self, val):
        """check if any rule passes for a given value"""
        for rule in self._rules:
            if self._validate_rule(rule, val):
                return True
        return False

    def day_a_find_bad_values(self):
        bad_vals = []
        for ticket in self._other_tickets:
            for val in ticket:
                if not self.validate_val(val):
                    bad_vals.append(val)
        return sum(bad_vals), bad_vals

    def find_good_tickets(self):
        good_tickets = []
        for ticket in self._other_tickets:
            good_ticket = True
            for val in ticket:
                if not self.validate_val(val):
                    good_ticket = False
                    break
            if good_ticket:
                good_tickets.append(ticket)
        return good_tickets

    def match_labels(self):
        good_tickets = self.find_good_tickets()
        print("good tickets found:", len(good_tickets))
        rule_matches = {}
        while len(rule_matches) < len(good_tickets[0]):
            for column in range(len(good_tickets[0])):
                if column in rule_matches.values():
                    continue
                potential_rules = list(
                    set(self._rules.keys()) - set(rule_matches.keys())
                )
                ticket_id = 0
                while len(potential_rules) > 1 and ticket_id < len(good_tickets):
                    value = good_tickets[ticket_id][column]
                    for rule in self._rules.keys():
                        if rule not in potential_rules:
                            continue
                        if not self._validate_rule(rule, value):
                            potential_rules.remove(rule)
                    ticket_id += 1
                if len(potential_rules) == 1:
                    rule_matches[potential_rules[0]] = column
        return rule_matches

    def day_b_get_my_ticket(self):
        my_ticket = {}
        rule_matches = self.match_labels()
        print("rules are:", rule_matches)
        for rule in rule_matches:
            my_ticket[rule] = self._my_ticket[rule_matches[rule]]
        return my_ticket

    def day_b_get_result(self):
        my_ticket = self.day_b_get_my_ticket()
        print("my ticket is:", my_ticket)
        mult = 1
        for key in my_ticket:
            if key.startswith("departure"):
                mult = mult * my_ticket[key]
        return mult


if __name__ == "__main__":
    d16 = TicketCheckerDay16("input_data.txt")
    print("day16a:", d16.day_a_find_bad_values())
    print("day16b:", d16.day_b_get_result())
