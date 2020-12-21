import numpy


class Tile:
    def __init__(self, data):
        self.tile_number = int(data[0][5:-2])
        self.tile = [line.strip() for line in data[1:11]]
        self.edges = {
            "n": self.tile[0],
            "s": self.tile[-1],
            "w": "".join([self.tile[i][0] for i in range(10)]),
            "e": "".join([self.tile[i][9] for i in range(10)]),
        }
        self._neighbours = []
        self._neighbours_direction = {}

    def _opposite_direction(self, direction):
        return {"n": "s", "s": "n", "e": "w", "w": "e"}[direction]

    def add_neighbour(self, edge, neighbour):
        if neighbour not in self._neighbours:
            self._neighbours.append(neighbour)
            self._neighbours_direction[edge] = neighbour
            neighbour.add_neighbour(edge, self)

    def is_corner(self):
        return len(self._neighbours) == 2

    def is_top_left_corner(self):
        return (
            len(self._neighbours) == 2
            and self.get_neighbour("e")
            and self.get_neighbour("s")
        )

    def id_if_corner(self):
        return self.tile_number if self.is_corner() else 1

    def _get_dir_flipped_of_edge(self, edge):
        flipped = False
        for dir, test_edge in self.edges.items():
            if test_edge == edge:
                return False, dir
            elif test_edge[::-1] == edge:
                return True, dir
        raise Exception("edge not found in tile", edge, self, self.edges)

    def get_neighbour_for_edge(self, edge):
        if edge[::-1] in self._neighbours_direction:
            edge = edge[::-1]
        return self._neighbours_direction.get(edge)

    def pop_neighbour_for_edge(self, edge):
        if edge[::-1] in self._neighbours_direction:
            edge = edge[::-1]
        return edge, self._neighbours_direction.pop(edge)

    def get_neighbour(self, direction):
        edge = self.edges[direction]
        return self.get_neighbour_for_edge(edge)

    def _swap_neighbours(self, dir_1, dir_2):
        edge_1, neighbour_1 = self.pop_neighbour_for_edge(self.edges[dir_1])
        edge_2, neighbour_2 = self.pop_neighbour_for_edge(self.edges[dir_2])
        if neighbour_1:
            self._neighbours_direction[edge_2] = neighbour_1
        if neighbour_2:
            self._neighbours_direction[edge_1] = neighbour_2

    def flip_horizontal(self):
        self.edges["e"], self.edges["w"] = self.edges["w"], self.edges["e"]
        self.edges["n"] = self.edges["n"][::-1]
        self.edges["s"] = self.edges["s"][::-1]
        for i in range(len(self.tile)):
            self.tile[i] = self.tile[i][::-1]

    def flip_vertical(self):
        self.edges["n"], self.edges["s"] = self.edges["s"], self.edges["n"]
        self.edges["e"] = self.edges["e"][::-1]
        self.edges["w"] = self.edges["w"][::-1]
        self.tile = self.tile[::-1]

    def _get_270_x(self, x, y):
        return 9 - y

    def _get_270_y(self, x, y):
        return x

    def _get_90_x(self, x, y):
        return y

    def _get_90_y(self, x, y):
        return 9 - x

    def rotate_90(self):
        movements = {"s": "w", "w": "n", "n": "e", "e": "s"}
        flip = ["e", "w"]
        new_edges = {}
        for direction in self.edges:
            edge = self.edges[direction]
            if direction in flip:
                edge = edge[::-1]
            new_edges[movements[direction]] = edge
        self.edges = new_edges
        self.tile = [
            "".join(
                [
                    self.tile[self._get_90_y(x, y)][self._get_90_x(x, y)]
                    for x in range(10)
                ]
            )
            for y in range(10)
        ]

    def rotate_270(self):
        movements = {"w": "s", "s": "e", "e": "n", "n": "w"}
        flip = ["s", "n"]
        new_edges = {}
        for direction in self.edges:
            edge = self.edges[direction]
            if direction in flip:
                edge = edge[::-1]
            new_edges[movements[direction]] = edge

        self.edges = new_edges
        self.tile = [
            "".join(
                [
                    self.tile[self._get_270_y(x, y)][self._get_270_x(x, y)]
                    for x in range(10)
                ]
            )
            for y in range(10)
        ]

    def rotate_180(self):
        self.flip_horizontal()
        self.flip_vertical()

    def _assert_edges(self):
        if self.tile[0] != self.edges["n"]:
            breakpoint()
            raise Exception("Invalid edge for north", self.edges, self.tile)
        if self.tile[9] != self.edges["s"]:
            raise Exception("Invalid edge for south", self.edges, self.tile)
        if "".join([self.tile[i][0] for i in range(10)]) != self.edges["w"]:
            raise Exception("Invalid edge for west", self.edges, self.tile)
        if "".join([self.tile[i][9] for i in range(10)]) != self.edges["e"]:
            raise Exception("Invalid edge for east", self.edges, self.tile)

    def transform_for_north_edge(self, edge):
        flipped, dir = self._get_dir_flipped_of_edge(edge)
        if dir == "n" and not flipped:
            pass
        elif dir == "n" and flipped:
            self.flip_horizontal()
        elif dir == "s" and not flipped:
            self.flip_vertical()
        elif dir == "s" and flipped:
            self.rotate_180()
        elif dir == "e" and not flipped:
            self.rotate_270()
        elif dir == "e" and flipped:
            self.rotate_270()
            self.flip_horizontal()
        elif dir == "w" and not flipped:
            self.rotate_90()
            self.flip_horizontal()
        else:  # dir == "w" and flipped:
            self.rotate_90()
        if self.edges["n"] != edge:
            raise Exception("transformation screwed up somewhere")
        self._assert_edges()

    def transform_for_west_edge(self, edge):
        flipped, dir = self._get_dir_flipped_of_edge(edge)
        if dir == "w" and not flipped:
            pass
        elif dir == "w" and flipped:
            self.flip_vertical()
        elif dir == "e" and not flipped:
            self.flip_horizontal()
        elif dir == "e" and flipped:
            self.rotate_180()
        elif dir == "n" and not flipped:
            self.flip_horizontal()
            self.rotate_270()
        elif dir == "n" and flipped:
            self.rotate_270()
        elif dir == "s" and not flipped:
            self.rotate_90()
        else:  # dir == "s" and flipped:
            self.flip_horizontal()
            self.rotate_90()

        if self.edges["w"] != edge:
            raise Exception("transformation screwed up somewhere")
        self._assert_edges()


class TileMatcherDay20:
    def __init__(self, filename):
        self._tiles = []
        self._ordered_tiles = []
        self._edges_to_match = {}
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            data = f.readlines()

        i = 0
        while i < len(data):
            self._tiles.append(Tile(data[i : i + 11]))
            i += 12

    def _build_edges(self):
        for tile in self._tiles:
            for dir, edge in tile.edges.items():
                if edge[::-1] in self._edges_to_match:
                    edge = edge[::-1]
                self._edges_to_match.setdefault(edge, [])
                self._edges_to_match[edge].append((dir, tile))

    def match_edges(self):
        self._build_edges()
        for edge_name, edges in self._edges_to_match.items():
            if len(edges) > 2:
                print("Got multiple tiles that fit edge", edge_name, edges)
            elif len(edges) == 2:
                direction, first_tile = edges[0]
                _, second_tile = edges[1]
                first_tile.add_neighbour(edge_name, second_tile)

    def day_a(self):
        self.match_edges()
        return numpy.product([tile.id_if_corner() for tile in self._tiles])

    def _find_top_left_corner(self):
        for tile in self._tiles:
            if tile.is_top_left_corner():
                return tile

    def layout_tiles(self):
        starting_tile = self._find_top_left_corner()
        print("starting tile is:", starting_tile.tile_number)
        self._ordered_tiles = [[starting_tile]]
        while (
            sum([len(ordered_tiles_row) for ordered_tiles_row in self._ordered_tiles])
        ) < len(self._tiles):
            if next_neighbour := self._ordered_tiles[-1][-1].get_neighbour("e"):
                old_neighbour = self._ordered_tiles[-1][-1]
                next_neighbour.transform_for_west_edge(old_neighbour.edges["e"])
                self._ordered_tiles[-1].append(next_neighbour)
            elif next_neighbour := self._ordered_tiles[-1][0].get_neighbour("s"):
                old_neighbour = self._ordered_tiles[-1][0]
                next_neighbour.transform_for_north_edge(old_neighbour.edges["s"])
                self._ordered_tiles.append([next_neighbour])
            else:
                print("should be done")

    def build_image(self):
        self._image = [
            list("".join([tiles_row[j].tile[i][1:9] for j in range(len(tiles_row))]))
            for i in range(1, 9)
            for tiles_row in self._ordered_tiles
        ]

    def _flip_image_horizontally(self):
        self._image = [self._image[y][::-1] for y in range(len(self._image))]

    def _flip_image_vertically(self):
        self._image = self._image[::-1]

    def _rotate_image_90(self):
        self._image = [
            [self._image[len(self._image) - y - 1][x] for y in range(len(self._image))]
            for x in range(len(self._image[0]))
        ]

    def _replace_o_with_hash(self):
        for y in range(len(self._image)):
            for x in range(len(self._image[y])):
                if self._image[y][x] == "O":
                    self._image[y][x] = "#"

    def day_b(self):
        self.match_edges()
        self.layout_tiles()
        self.build_image()
        for vertical in range(2):
            for horizontal in range(2):
                for rotations in range(4):
                    dragons = self.find_dragons()
                    if dragons > 0:
                        print("found ", dragons, "dragons")
                        print(
                            "total waves:", sum([row.count("#") for row in self._image])
                        )
                        self._replace_o_with_hash()
                        self._rotate_image_90()
                    else:
                        print("rotating because no dragons")
                        self._rotate_image_90()
                print("trying agian with flipped image vertical")
                self._flip_image_vertically()
            print("trying again with flipped image horizontally")
            self._flip_image_horizontally()
        return sum([row.count("#") for row in self._image])

    def _o_replace_image(self, x, y, dragon):
        for d_y in range(len(dragon)):
            for d_x in range(len(dragon[d_y])):
                if dragon[d_y][d_x] == "#":
                    self._image[y + d_y][x + d_x] = "O"

    def find_dragons(self):
        dragon = [
            "                  #",
            "#    ##    ##    ###",
            " #  #  #  #  #  #",
        ]
        dragons = 0
        for y in range(len(self._image) - len(dragon)):
            for x in range(len(self._image[0]) - len(dragon[0])):
                is_dragon = True
                for d_y in range(len(dragon)):
                    for d_x in range(len(dragon[d_y])):
                        if (
                            dragon[d_y][d_x] == "#"
                            and self._image[y + d_y][x + d_x] != "#"
                        ):
                            is_dragon = False
                            break
                    if not is_dragon:
                        break
                if is_dragon:
                    dragons += 1
                    self._o_replace_image(x, y, dragon)
        return dragons


if __name__ == "__main__":
    d20a = TileMatcherDay20("input_data.txt")
    print("d20a:", d20a.day_a())

    d20b = TileMatcherDay20("input_data.txt")
    print("d20b:", d20b.day_b())
