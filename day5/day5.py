class BinaryPlaneDecoder:
    @staticmethod
    def decode_line(line):
        column = line[0:7]
        seat = line[7:10]
        column = column.replace("F", "0")
        column = column.replace("B", "1")
        seat = seat.replace("R", "1")
        seat = seat.replace("L", "0")
        column_num = int(column, 2)
        seat_num = int(seat, 2)
        return column_num, seat_num, column_num * 8 + seat_num


class BinaryPlaneSearch:
    def __init__(self, filename):
        self._plane_ticket_ids = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            self._plane_tickets.append(BinaryPlaneDecoder.decode_line(line)[2])

    def find_highest_ticket(self):
        max_id = 0
        for ticket in self._plane_ticket_ids:
            max_id = max(max_id, ticket)
        return max_id

    def find_missing_ticket(self):
        return set(range(100, 911)).difference(set(self._plane_ticket_ids))


if __name__ == "__main__":
    bps = BinaryPlaneSearch("input_data.txt")
    day5a_result = bps.find_highest_ticket()
    print("day5a:", day5a_result)
    day5b_result = bps.find_missing_ticket()
    print("day5b:", day5b_result)
