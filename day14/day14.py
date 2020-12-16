class MemoryMakerDay14:
    def __init__(self, filename):
        self._instructions = []
        self._build_data(filename)
        self._memory = {}

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._instructions = f.readlines()

    def _set_bit_high(self, val, bit):
        return val | (1 << bit)

    def _set_bit_low(self, val, bit):
        return val & (~(1 << bit))

    def _apply_mask_a(self, val, mask):
        for i, x in enumerate(mask[::-1]):
            if x == "1":
                val = self._set_bit_high(val, i)
            elif x == "0":
                val = self._set_bit_low(val, i)
        return val

    def day_a(self):
        self._memory = {}
        mask = "X" * 35
        for instruction in self._instructions:
            left, right = instruction.split(" = ")
            if left == "mask":
                mask = right.strip()
            else:
                index = int(left[4:-1])
                self._memory[index] = self._apply_mask_a(int(right), mask)
        return sum(self._memory.values())

    def _apply_mask_b(self, val, mask):
        ret = [val]
        for i, x in enumerate(mask[::-1]):
            if x == "1":
                for j in range(len(ret)):
                    ret[j] = self._set_bit_high(ret[j], i)
            if x == "X":
                for j in range(len(ret)):
                    ret[j] = self._set_bit_low(ret[j], i)
                ret2 = ret.copy()
                for j in range(len(ret2)):
                    ret2[j] = self._set_bit_high(ret2[j], i)
                ret.extend(ret2)
        return ret

    def day_b(self):
        self._memory = {}
        mask = "0" * 35
        for instruction in self._instructions:
            left, right = instruction.split(" = ")
            if left == "mask":
                mask = right.strip()
            else:
                index = int(left[4:-1])
                value = int(right)
                indices = self._apply_mask_b(index, mask)
                for i in indices:
                    self._memory[i] = value
                # print("setting", index, mask, right, indices)
        return sum(self._memory.values())


if __name__ == "__main__":
    d14 = MemoryMakerDay14("input_data.txt")
    print("d14a:", d14.day_a())
    print("d14b:", d14.day_b())