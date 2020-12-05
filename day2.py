class Day2:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    @staticmethod
    def _delimiter(line: list) -> tuple:
        line = line.split(" ")
        low, high = [int(num) for num in line[0].split("-")]
        letter = line[1][0:-1]
        password = line[2]
        return (low, high, letter, password)

    def part1(self) -> int:
        output = 0
        for line in self.key:
            low, high, letter, password = self._delimiter(line)
            letter_count = password.count(letter)
            if letter_count >= low and letter_count <= high:
                output += 1
        return output

    def part2(self) -> int:
        output = 0
        for line in self.key:
            idx1, idx2, letter, password = self._delimiter(line)
            if password[idx1 - 1] == letter and password[idx2 - 1] == letter:
                continue
            if password[idx1 - 1] == letter or password[idx2 - 1] == letter:
                output += 1
        return output


if __name__ == "__main__":
    day2 = Day2("day2.txt")
    print(day2.part1())
    print(day2.part2())
