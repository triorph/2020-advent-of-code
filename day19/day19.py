from copy import copy


class RuleCheckerDay19:
    def __init__(self, filename):
        self._rules = {}
        self._data = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if ":" not in line:
                self._data = [line.strip() for line in lines[i + 1 :]]
                break
            else:
                rule_name, rules = line.strip().split(": ")
                self._rules[rule_name.strip()] = rules.strip()

    def evaluate_rule(self, rule, data):
        if isinstance(data, str):
            data = [data]
        if len(data) == 0:
            return False, data
        if '"' in rule:
            valid_data = [d[1:] for d in data if len(d) > 0 and d[0] == rule[1]]
            return len(valid_data) > 0, valid_data
        rules = rule.split("|")
        valid_data = []
        for or_rule in rules:
            data_copy = copy(data)
            valid_rule = True
            for subrule in or_rule.strip().split(" "):
                ret, data_copy2 = self.evaluate_rule(
                    self._rules[subrule.strip()], data_copy
                )
                data_copy = data_copy2
                if not ret:
                    valid_rule = False
                    break
            if valid_rule:
                valid_data.extend(data_copy)
        return len(valid_data) > 0, valid_data

    def evaluate_rule_zero(self, data):
        ret, data = self.evaluate_rule(self._rules["0"], data)
        return ret and "" in data

    def day_a(self):
        return [self.evaluate_rule_zero(line) for line in self._data].count(True)

    def add_day_b_rules(self):
        self._rules["8"] = "42 | 42 8"
        self._rules["11"] = "42 31 | 42 11 31"

    def day_b(self):
        self.add_day_b_rules()
        return self.day_a()


if __name__ == "__main__":
    d19 = RuleCheckerDay19("input_data.txt")
    print("d19a:", d19.day_a())
    print("d19b:", d19.day_b())
