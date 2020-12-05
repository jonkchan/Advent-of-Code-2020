class Day6:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def part1(self):
        return

    def part2(self):
        return


if __name__ == "__main__":
    day6 = Day6("day6.txt")
    print(day6.part1())
    print(day6.part2())
