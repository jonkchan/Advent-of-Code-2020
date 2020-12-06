class Day6:

    def __init__(self, filename):
        # with open(filename, 'r') as file:
        #     self.key = file.read().splitlines()
        with open(filename, 'r') as file:
            self.key = self.key_delimiter(file.read())

    @staticmethod
    def key_delimiter(key: str) -> list:
        output = []
        group = []
        for line in key.splitlines():
            if line == "":
                output.append(group)
                group = []
                continue

            group.append(line)

        if group:
            output.append(group)

        return output

    def part1(self) -> int:
        total_sum = 0
        for group in self.key:
            consolidated_responses = "".join([response for response in group])
            total_sum += len(set(consolidated_responses))
        return total_sum

    def part2(self):
        total_sum = 0
        for group in self.key:
            response_tracker = {}
            for response in group:
                for answer in response:
                    if answer not in response_tracker:
                        response_tracker[answer] = 0
                    response_tracker[answer] += 1

            total_sum += sum([1 for i in response_tracker if response_tracker[i] == len(group)])
        return total_sum


if __name__ == "__main__":
    day6 = Day6("day6.txt")
    print(day6.part1())
    print(day6.part2())
