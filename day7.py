class Day7:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def check_valid_bag(self, bag_color: str, tracker: dict) -> bool:
        if bag_color in tracker and tracker[bag_color]:
            return True

        return False

    def track_rule_indexes(self) -> dict:
        tracker = {}
        for idx, bag_rule in enumerate(self.key):
            bag_rule = bag_rule.split(" ")
            bag_color = " ".join(bag_rule[:3])
            tracker[bag_color] = idx
        return tracker

    def part1(self) -> int:
        total_count = 0
        rule_indexes = self.track_rule_indexes
        tracker = {}
        for rule in self.key:
            rule = rule.split(" ")
            bag_color = " ".join(rule[:3])
            queue = [bag_color]

            while queue:
                current_bag = queue.pop(0)
                if self.check_valid_bag(current_bag, tracker):
                    total_count += 1
                sub_bag = " ".join(rule[-3:])[:-1]
                queue.append(sub_bag)

        return total_count

    def part2(self):
        return


if __name__ == "__main__":
    day7 = Day7("day7test.txt")
    # print(day7.part1())
    day7.track_rule_indexes()
    # print(day7.part2())
