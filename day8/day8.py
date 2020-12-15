from copy import deepcopy


class AssemblyExecutor:
    def __init__(self, filename):
        self._code = []
        self._code_line_calls = {}
        self._executor = 0
        self._accumulator = 0
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._code = f.readlines()

    def _day_a_check_break(self):
        self._code_line_calls.setdefault(self._executor, 0)
        return self._code_line_calls[self._executor] >= 1

    def day_a_run_until_repeat(self):
        self._executor = 0
        self._accumulator = 0
        self._code_line_calls = {}
        while not self._day_a_check_break() and self._executor < len(self._code):
            self._run_current_line()
        return self._accumulator

    def _get_instruction_value(self, code_line):
        instruction, value = code_line.strip().split(" ")
        value = int(value)
        return instruction, value

    def _run_current_line(self):
        self._code_line_calls[self._executor] += 1
        instruction, value = self._get_instruction_value(self._code[self._executor])
        if instruction == "jmp":
            self._executor += value
        else:
            if instruction == "acc":
                self._accumulator += value
            self._executor += 1

    def replace_ops(self):
        base_code = deepcopy(self._code)
        for i, line in enumerate(base_code):
            self._code = deepcopy(base_code)
            instruction, value = self._get_instruction_value(self._code[i])
            if instruction == "jmp":
                self._code[i] = f"nop, {value}"
            elif instruction == "nop":
                self._code[i] = f"jmp, {value}"
            else:
                continue
            self.day_a_run_until_repeat()
            if self._executor >= len(self._code):
                return self._accumulator


if __name__ == "__main__":
    d8 = AssemblyExecutor("input_data.txt")
    print("d8a:", d8.day_a_run_until_repeat())
    print("d8b:", d8.replace_ops())
