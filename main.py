
import datetime
import Numerology


def main():

    while True:
        try:
            name = input("Whats your full name? ").upper()
            if not name:
                raise ValueError('Empty string')
            break
        except ValueError:
            main()
    while True:
        dob = input("Whats your date of birth, MM-DD-YYYY format ")
        try:
            datetime.datetime.strptime(dob, "%m-%d-%Y")
            break
        except ValueError:
            print("Please input correct date format")

    your_numerology = Numerology.Numerology(name, dob)
    life_path = your_numerology.get_life_path(dob)
    soul_num = your_numerology.get_soul(name)
    personality_num = your_numerology.get_personality(name)
    print(f"Test Name: {your_numerology.get_name()}")
    print(f"Test DOB: {your_numerology.get_dob()}")
    print(f"Life Path Number: {life_path}")
    print(f"Birth Day Number: {your_numerology.get_birthday(dob)}")
    print(f"Attitude Number: {your_numerology.get_attitude(dob)}")
    print(f"Soul Number: {soul_num}")
    print(f"Personality Number: {personality_num}")
    print(f"Power Name Number: {your_numerology.get_power_name(soul_num, personality_num)}")
    should_continue = input("Do you want to play again? Put y for yes or n for no: ").lower()
    if should_continue == "y":
        main()
    else:
        exit()


main()

