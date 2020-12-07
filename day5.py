class Day5:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    @staticmethod
    def _space_finder(directions: str, num_of_spaces: int) -> int:
        spaces = [i for i in range(0, num_of_spaces)]
        for direction in directions:
            midpoint = len(spaces)//2
            if direction in ["F", "L"]:
                spaces = spaces[:midpoint]
            elif direction in ["B", "R"]:
                spaces = spaces[midpoint:]
        return min(spaces)

    @staticmethod
    def _calculate_seat_id(boarding_pass: str) -> int:
        # First 7 characters will either be F or B to determine the seat row
        # Last 3 characters will either be L or R to determine the seat column
        row_directions, col_directions = boarding_pass[:7], boarding_pass[-3:]

        row = Day5._space_finder(row_directions, 128)
        col = Day5._space_finder(col_directions, 8)

        # Unique seat ID found by multiplying seat row by 8 then adding seat column
        seat_id = (row * 8) + col
        return seat_id

    def part1(self) -> int:
        highest_seat_id = 0
        for boarding_pass in self.key:
            seat_id = self._calculate_seat_id(boarding_pass)

            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

        return highest_seat_id

    def part2(self) -> int:
        seat_ids = [self._calculate_seat_id(
            boarding_pass) for boarding_pass in self.key]

        seat_ids = sorted(seat_ids)

        for idx, seat_id in enumerate(seat_ids, seat_ids[0]):
            if seat_id != idx:
                return idx


if __name__ == "__main__":
    day5 = Day5("day5.txt")
    print(day5.part1())
    print(day5.part2())
