class BagTree:
    def __init__(self, filename):
        self._bag_tree = {}
        self._build_data(filename)

    def _extract_colour(self, bagname):
        if bagname[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            bagname = bagname[bagname.find(" ") + 1 :]
        for ending in ["bag", "bags", "bags.", "bag."]:
            if bagname.endswith(ending):
                bagname = bagname[: bagname.find(ending)].strip()
        return bagname

    def _extract_number(self, bagname):
        return int(bagname[: bagname.find(" ")].strip())

    def _build_children(self, container_str):
        if container_str == "no other bags.":
            return []
        else:
            return [
                (self._extract_colour(bagname_str), self._extract_number(bagname_str))
                for bagname_str in container_str.split(", ")
            ]

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            bagname, container = line.strip().split(" contain ")
            bagname = self._extract_colour(bagname.strip())
            self._bag_tree[bagname] = self._build_children(container.strip())

    def find_parents(self, bagname, ret=set()):
        for key, value in self._bag_tree.items():
            just_value = [v[0] for v in value]
            if bagname in just_value and key not in ret:
                ret.add(key)
                ret.update(self.find_parents(key, ret))
        return ret

    def find_children_quantities(self, bagname):
        children = self._bag_tree[bagname]
        print("checking children for bagname:", children, bagname)
        ret = 1 + sum(
            [
                count * self.find_children_quantities(_bagname)
                for _bagname, count in children
            ]
        )
        print("returning", ret, bagname)
        return ret


if __name__ == "__main__":
    d7 = BagTree("input_data.txt")
    print(d7._bag_tree)
    print("d7a:", len(d7.find_parents("shiny gold")))
    print(
        "d7b:", d7.find_children_quantities("shiny gold") - 1
    )  # don't include the shiny bag in the final answer
