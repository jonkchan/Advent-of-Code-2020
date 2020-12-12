class Day12:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def part1(self) -> int:
        x, y = 0, 0
        direction = 0
        directions = ["E", "S", "W", "N"]
        for instruction in self.key:
            action = instruction[0]
            value = int(instruction[1:])

            if action in ["L", "R"]:
                value //= 90
                if action == "L":
                    value *= -1
                direction = (direction + value) % 4
                continue

            if action == "F":
                action = directions[direction]

            if action == "N":
                y += value
            elif action == "S":
                y -= value
            elif action == "W":
                x -= value
            elif action == "E":
                x += value

        return abs(x) + abs(y)

    def part2(self):
        waypt_x, waypt_y = 10, 1
        ship_x, ship_y = 0, 0
        for instruction in self.key:
            action = instruction[0]
            value = int(instruction[1:])

            if action in ["L", "R"]:
                if value == 180:
                    waypt_x *= -1
                    waypt_y *= -1
                    continue

                is_left = 1 if action == "L" else -1
                is_right = 1 if action == "R" else -1

                if value == 90:
                    waypt_x, waypt_y = (
                        waypt_y * is_right), (waypt_x * is_left)
                elif value == 270:
                    waypt_x, waypt_y = (
                        waypt_y * is_right * -1), (waypt_x * is_left * -1)
                continue

            if action == "F":
                ship_x += waypt_x * value
                ship_y += waypt_y * value
                continue

            if action == "N":
                waypt_y += value
            elif action == "S":
                waypt_y -= value
            elif action == "W":
                waypt_x -= value
            elif action == "E":
                waypt_x += value

        return abs(ship_x) + abs(ship_y)


if __name__ == "__main__":
    day12 = Day12("day12.txt")
    print(day12.part1())
    print(day12.part2())
