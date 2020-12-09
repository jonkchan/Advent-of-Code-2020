class Day9:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = [int(i) for i in file.read().splitlines()]

    def validate_two_sum(self, target: int, numbers: list) -> bool:
        tracker = {}
        for num in numbers:
            difference = target - num
            if difference in tracker:
                return True
            else:
                tracker[num] = True
        return False

    def part1(self, preamble: int = 25) -> int:
        idx = preamble
        while idx < len(self.key):
            num = self.key[idx]
            previous_numbers = self.key[idx - preamble: idx]

            if self.validate_two_sum(num, previous_numbers):
                idx += 1
                continue

            return num

    def part2(self, target: int) -> int:
        for idx, num in enumerate(self.key):
            total = 0
            smallest_num, largest_num = float('inf'), float('-inf')
            while total < target:
                current_num = self.key[idx]
                if current_num > largest_num:
                    largest_num = current_num
                if current_num < smallest_num:
                    smallest_num = current_num
                total += current_num
                idx += 1

            if total == target:
                return smallest_num + largest_num


if __name__ == "__main__":
    day9 = Day9("day9.txt")
    part1_value = day9.part1()

    print(part1_value)
    print(day9.part2(part1_value))
