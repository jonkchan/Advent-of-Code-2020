class Day3:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def part1(self, right_slope: int, down_slope: int) -> int:
        output = 0
        row_length = len(self.key[0])

        position = 0
        for i in range(0, len(self.key), down_slope):
            if i == 0:
                continue

            row = self.key[i]
            position += right_slope
            position %= row_length

            if row[position] == "#":
                output += 1

        return output

    def part2(self) -> int:
        slope1 = self.part1(1, 1)
        slope2 = self.part1(3, 1)
        slope3 = self.part1(5, 1)
        slope4 = self.part1(7, 1)
        slope5 = self.part1(1, 2)
        return slope1 * slope2 * slope3 * slope4 * slope5


if __name__ == "__main__":
    day3 = Day3("day3.txt")
    print(day3.part1(3, 1))
    print(day3.part2())
