class Day7:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def part1(self):
        return

    def part2(self):
        return


if __name__ == "__main__":
    day7 = Day7("day7.txt")
    print(day7.part1())
    print(day7.part2())
