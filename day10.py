class Day10:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = [int(i) for i in file.read().splitlines()]

    def part1(self) -> int:
        jolt_rating = 0
        diff_count = {1: 0, 3: 1}

        for adapter in sorted(self.key):
            if adapter < jolt_rating:
                continue

            if adapter <= jolt_rating + 3:
                diff = adapter - jolt_rating
                diff_count[diff] += 1
                jolt_rating = adapter

        return diff_count[1] * diff_count[3]

    def part2(self):
        return


if __name__ == "__main__":
    day10 = Day10("day10.txt")
    print(day10.part1())
    # print(day10.part2())
