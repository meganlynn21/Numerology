class Numerology:
    # First part of the code to set up and store
    # and protect/Encapsulate the name,dob, conversion_vowels, and conversion_consonants :
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob
        self.__conversion_vowels = {"A": 1, "U": 3, "E": 5, "O": 6, "I": 9, " ": 0}
        self.__conversion_consonants = {"S": 1, "J": 1, "B": 2, "K": 2, "T": 2, "C": 3, "D": 4, "M": 4, "V": 4, "W": 5,
                                        "N": 5, "X": 6, "F": 6, "G": 7, "P": 7, "Y": 7, "H": 8, "Q": 8, "Z": 8, "R": 9,
                                        " ": 0}

    def get_name(self):
        """Returns the subjects name"""
        return self.__name

    def get_dob(self):
        """Returns the subjects date of birth"""
        return self.__dob

    # Adds the birth month and the birthdate from dob, then takes the sum of that number and reduces it
    def get_attitude(self, dob):
        """Returns the computed attitude number"""
        split_dob = dob.split('-')
        join_dob = ''.join(split_dob)
        day_and_month = join_dob[0:4]
        result = list(map(int, str(day_and_month)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)

    # Extracts the day from the dob and adds the 2 numbers together, then reduces the sum of that number
    def get_birthday(self, dob):
        """Returns the computed birthday number"""
        split_dob = dob.split('-')
        join_dob = ''.join(split_dob)
        day = join_dob[2:4]
        result = list(map(int, str(day)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)

    # Is computed by taking all digits in the dob and adding them together then reducing the sum
    def get_life_path(self, num):
        """Returns the computed life path number"""
        split_dob = num.split('-')
        join_dob = ''.join(split_dob)
        nums = int(join_dob)
        result = list(map(int, str(nums)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)

    # Takes all the consonants in name and uses the consonant dictionary to get the number for that letter
    # then adds those letters together and reduces the sum
    def get_personality(self, name):
        """ Returns the computed personality number"""
        res = 0
        for letter in name:
            if letter in self.__conversion_consonants:
                res += self.__conversion_consonants[letter]
        str_res = str(res)
        split_name = list(str_res)
        new_list = []
        for x in split_name:
            new_list.append(x)
        join_list = ''.join(new_list)
        nums = int(join_list)
        result = list(map(int, str(nums)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)

    # Is computed by adding the soul and personality number together then reducing that number
    def get_power_name(self, soul, personality):
        """Returns the computed power name number"""
        total = soul + personality
        str_res = str(total)
        split_name = list(str_res)
        new_list = []
        for x in split_name:
            new_list.append(x)
        join_list = ''.join(new_list)
        nums = int(join_list)
        result = list(map(int, str(nums)))
        sum_of_list = sum(result)
        return sum_of_list

    # Takes all the vowels in name and uses the vowel dictionary to get the number for that letter
    # then adds those letters together and reduces the sum
    def get_soul(self, name):
        """ returns the computed soul number"""
        res = 0
        for letter in name:
            if letter in self.__conversion_vowels:
                res += self.__conversion_vowels[letter]
        str_res = str(res)
        split_name = list(str_res)
        new_list = []
        for x in split_name:
            new_list.append(x)
        join_list = ''.join(new_list)
        nums = int(join_list)
        result = list(map(int, str(nums)))
        sum_of_list = sum(result)
        return sum_of_list

