class Day4:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.key = self.key_delimiter(file.read())

    @staticmethod
    def key_delimiter(key: str) -> list:
        output = []
        passport = {}
        for line in key.splitlines():
            if line == "":
                output.append(passport)
                passport = {}
                continue

            for fields in line.split(" "):
                fields = fields.split(":")
                passport[fields[0]] = fields[1]

        # Capture last passport from key string
        if passport:
            output.append(passport)

        return output

    def part1(self):
        output = 0
        for passport in self.key:

            is_valid_passport = True

            # Check if all required fields are present in passport
            for field in Day4.required_fields:
                if field not in passport:
                    is_valid_passport = False
                    break

            if is_valid_passport:
                output += 1

        return output

    @staticmethod
    def _validate_num_in_range(num: int, low: int, high: int) -> bool:
        return num >= low and num <= high

    @staticmethod
    def _field_validation(field_name: str, field_value: any) -> bool:
        if field_name == "byr":
            return Day4._validate_num_in_range(int(field_value), 1920, 2002)
        elif field_name == "iyr":
            return Day4._validate_num_in_range(int(field_value), 2010, 2020)
        elif field_name == "eyr":
            return Day4._validate_num_in_range(int(field_value), 2020, 2030)
        elif field_name == "hgt":
            valid_unit = False
            for unit in ["cm", "in"]:
                if unit in field_value:
                    valid_unit = True
                    break

            if not valid_unit:
                return False

            measurement = int(field_value[0:len(field_value)-2])
            unit = field_value[-2:]
            if unit == "cm":
                return Day4._validate_num_in_range(measurement, 150, 193)
            elif unit == "in":
                return Day4._validate_num_in_range(measurement, 59, 76)

        elif field_name == "hcl":
            return field_value[0] == "#" and len(field_value) == 7
        elif field_name == "ecl":
            return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif field_name == "pid":
            return field_value.isdigit() and len(field_value) == 9

    def part2(self):
        output = 0
        for passport in self.key:

            is_valid_passport = True

            # Check if all required fields are present in passport
            for field in Day4.required_fields:
                if field not in passport:
                    is_valid_passport = False
                    break

                is_valid_passport = self._field_validation(
                    field, passport[field])

                if not is_valid_passport:
                    break

            if is_valid_passport:
                output += 1

        return output


if __name__ == "__main__":
    day4 = Day4("day4.txt")
    print(day4.part1())
    print(day4.part2())
