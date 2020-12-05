class Day1:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = [int(i) for i in file.read().splitlines()]

    def part1(self, target_sum: int) -> int:
        tracker = {}
        for num in self.key:
            difference = target_sum - num
            if difference in tracker:
                return num * difference
            tracker[num] = True

    def part2(self, target_sum: int) -> int:
        self.key.sort()
        for idx in range(len(self.key) - 2):
            left = idx + 1
            right = len(self.key) - 1
            while left < right:
                current_sum = self.key[idx] + self.key[left] + self.key[right]
                if current_sum == target_sum:
                    return self.key[idx] * self.key[left] * self.key[right]
                elif current_sum < target_sum:
                    left += 1
                elif current_sum > target_sum:
                    right -= 1


if __name__ == "__main__":
    day1 = Day1("day1.txt")
    print(day1.part1(2020))
    print(day1.part2(2020))
