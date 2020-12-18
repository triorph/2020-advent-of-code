class DayBPassportValidator:
    @staticmethod
    def _validate_birth_year(year_str):
        try:
            year = int(year_str)
            return year >= 1920 and year <= 2002
        except TypeError:
            return False

    @staticmethod
    def _validate_issue_year(year_str):
        try:
            year = int(year_str)
            return year >= 2010 and year <= 2020
        except TypeError:
            return False

    @staticmethod
    def _validate_expiry_year(year_str):
        try:
            year = int(year_str)
            return year >= 2020 and year <= 2030
        except TypeError:
            return False

    @staticmethod
    def _validate_height(height_str):
        try:
            height = int(height_str[:-2])
            unit = height_str[-2:]
            if unit == "cm":
                return height >= 150 and height <= 193
            elif unit == "in":
                return height >= 59 and height <= 76
            else:
                return False
        except (TypeError, IndexError):
            return False

    @staticmethod
    def _validate_hair_colour(hair_colour_str):
        if len(hair_colour_str) != 7 or hair_colour_str[0] != "#":
            return False
        for c in hair_colour_str[1:]:
            if c not in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            ]:
                print("hair colour fialed on letter", c)
                return False
        return True

    @staticmethod
    def _validate_eye_colour(eye_colour_str):
        return eye_colour_str in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    @staticmethod
    def _validate_passport_id(pid_str):
        if len(pid_str) != 9:
            return False
        for c in pid_str:
            if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False

        return True

    def validate_passport(self, passport):
        VALIDATOR_ALGORITHMS = {
            "byr": self._validate_birth_year,
            "iyr": self._validate_issue_year,
            "eyr": self._validate_expiry_year,
            "hgt": self._validate_height,
            "hcl": self._validate_hair_colour,
            "ecl": self._validate_eye_colour,
            "pid": self._validate_passport_id,
        }
        for key in VALIDATOR_ALGORITHMS:
            if key not in passport:
                return False
            if not VALIDATOR_ALGORITHMS[key](passport[key].strip()):
                return False
        return True


class PassportValidator:
    REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def __init__(self, filename):
        self._passports = []
        self.build_passports(filename)
        print("We have ", (len(self._passports)), "passports")

    def read_data(self, filename):
        with open(filename, "r") as f:
            return f.readlines()

    def build_passports(self, filename):
        current_passport = {}
        for line in self.read_data(filename):
            if line.strip() == "":
                self._passports.append(current_passport)
                current_passport = {}
            else:
                key_values = line.strip().split(" ")
                for key_value in key_values:
                    key, value = key_value.strip().split(":")
                    current_passport[key] = value

        self._passports.append(current_passport)

    def validate_passport_a(self, passport):
        return self.REQUIRED_FIELDS.issubset(set(passport.keys()))

    def validate_passport_b(self, passport):
        return DayBPassportValidator().validate_passport(passport)

    def validate_passports_a(self):
        count = 0
        for passport in self._passports:
            count += self.validate_passport_a(passport)

        return count

    def validate_passports_b(self):
        count = 0
        for passport in self._passports:
            count += self.validate_passport_b(passport)

        return count


if __name__ == "__main__":
    d4 = PassportValidator("input_data.txt")
    print("d4a:", d4.validate_passports_a())
    print("d4b:", d4.validate_passports_b())