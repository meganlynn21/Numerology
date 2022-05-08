

import datetime
import Numerology


def main():
    is_valid = True
    while is_valid:
        try:
            name = input("whats your full name? ").upper()
            if not name:
                raise ValueError('empty string')
            break
        except ValueError:
            main()
    while is_valid:
        dob = input("whats your date of birth, MM-DD-YYYY format ")
        try:
            datetime.datetime.strptime(dob, "%m-%d-%Y")
            break
        except ValueError:
            print("please input correct date format")

    your_numerology = Numerology.Numerology(name, dob)
    life_path = your_numerology.get_life_path(dob)
    print(f"Test Name: {your_numerology.get_name()}")
    print(f"Test DOB: {your_numerology.get_dob()}")
    print(f"Life Path Number: {life_path}")
    print(f"Birth Day Number: {your_numerology.get_birthday(dob)}")
    print(f"Attitude Number: {your_numerology.get_attitude(dob)}")
    print(f"Soul Number: {your_numerology.get_soul(name)}")
    print(f"Personality Number: {your_numerology.get_personality(name)}")

main()

