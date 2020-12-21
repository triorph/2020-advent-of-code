class AllergenFinderDay21:
    def __init__(self, filename):
        self._data = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            first_bracket_pos = line.find("(")
            foods = line[:first_bracket_pos].strip().split(" ")
            allergens = line[first_bracket_pos + 10 :].strip("() \n").split(", ")
            self._data.append((foods, allergens))

    def _allergens_to_remove(self, allergen_possibilities):
        return sum([len(ap) for ap in allergen_possibilities.values()]) != len(
            allergen_possibilities
        )

    def _reduce_allergen_possibilities(self, allergen_possibilities):
        while self._allergens_to_remove(allergen_possibilities):
            for allergen, foods in allergen_possibilities.items():
                if len(foods) == 1:
                    # definitely the correct food, remove it from all other allergens
                    food = list(foods)[0]
                    allergen_possibilities[allergen] = list(foods)
                    for allergen2 in allergen_possibilities:
                        if allergen == allergen2:
                            continue
                        if food in allergen_possibilities[allergen2]:
                            allergen_possibilities[allergen2].remove(food)
        return allergen_possibilities

    def find_allergen_foods(self):
        allergen_possibilities = {}
        for food, allergens in self._data:
            for allergen in allergens:
                if allergen not in allergen_possibilities:
                    allergen_possibilities[allergen] = set(food)
                else:
                    allergen_possibilities[allergen] = allergen_possibilities[
                        allergen
                    ].intersection(set(food))
        return self._reduce_allergen_possibilities(allergen_possibilities)

    def _get_foods_that_are_allergens(self):
        allergen_possibilities = self.find_allergen_foods()
        return [food for foods in allergen_possibilities.values() for food in foods]

    def day_a(self):
        allergen_foods = self._get_foods_that_are_allergens()
        count = 0
        for foods, _ in self._data:
            for food in foods:
                if food not in allergen_foods:
                    count += 1
        return count

    def day_b(self):
        allergen_possibilities = self.find_allergen_foods()
        sorted_foods = []
        for key in sorted(allergen_possibilities.keys()):
            sorted_foods.append(list(allergen_possibilities[key])[0])
        return ",".join(sorted_foods)


if __name__ == "__main__":
    d21 = AllergenFinderDay21("input_data.txt")
    print("d21a:", d21.day_a())
    print("d21b:", d21.day_b())
