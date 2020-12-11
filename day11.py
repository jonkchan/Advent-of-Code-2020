class Day11:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().splitlines()

    def count_adjacent_occupancy(self, layout: list, y: int, x: int) -> int:
        count = 0
        for y_change in range(-1, 2):
            for x_change in range(-1, 2):
                # Protect against negative y indexing
                if y_change == -1 and y == 0:
                    continue

                # Protect against negative x indexing
                if x_change == -1 and x == 0:
                    continue

                # Skip counting middle seat
                if y_change == 0 and x_change == 0:
                    continue

                try:
                    if layout[y + y_change][x + x_change] == "#":
                        count += 1
                except IndexError:
                    pass

        return count

    def display_layout(self, layout) -> None:
        for row in layout:
            print(row)
        print("\n")

    def part1(self) -> int:
        layout = self.key
        previous_occupied_seat_count = 0
        occupied_seat_count = float('inf')

        while occupied_seat_count != previous_occupied_seat_count:
            updated_layout = []
            for row_idx, row in enumerate(layout):
                row_seating = ""
                for col_idx, seat in enumerate(row):
                    # Floor (.) never changes; seats don't move, and nobody sits on the floor
                    if seat == ".":
                        row_seating += "."
                        continue

                    adjacent_occupancy = self.count_adjacent_occupancy(
                        layout, row_idx, col_idx)

                    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                    if seat == "L" and adjacent_occupancy == 0:
                        seat_status = "#"
                    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                    elif seat == "#" and adjacent_occupancy >= 4:
                        seat_status = "L"
                    # Otherwise, the seat's state does not change.
                    else:
                        seat_status = seat

                    row_seating += seat_status

                updated_layout.append(row_seating)

            previous_occupied_seat_count = sum([i.count("#") for i in layout])

            # Update new seating layout and count occupied seats
            layout = updated_layout
            occupied_seat_count = sum([i.count("#") for i in layout])

        # Return count of occupied seats
        return occupied_seat_count

    def part2(self):
        return


if __name__ == "__main__":
    day11 = Day11("day11.txt")
    print(day11.part1())
    # print(day11.part2())
