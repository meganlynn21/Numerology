class Numerology:
    # First part of the code to set up and store
    # and protect/Encapsulate the name and dob :
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

        # Do the reading code here...
        # 11/24/202
        # iDay = int(self.__dob[0:2])
        # iMonth = int(self.__dob[3:5])
        # iYear = int(self.__dob[6:])
        #
        # sDateParts = self.__dob.split('/')
        # iDay = int(sDateParts[0])
        # iMonth = int(sDateParts[0])
        # iYear = int(sDateParts[0])

        # do more here...

    # coding the "getters"
    def get_name(self):
        """Returns the subjects name"""
        return self.__name

    def get_dob(self):
        """Returns the subjects date of birth"""
        return self.__dob

    def get_attitude(self, dob):
        """Returns the computed attitude number"""
        split_dob = dob.split('-')
        join_dob = ''.join(split_dob)
        day_and_month = join_dob[0:4]
        result = list(map(int, str(day_and_month)))
        return sum(result)

    def get_birthday(self, dob):
        """Returns the computed birthday number"""
        split_dob = dob.split('-')
        join_dob = ''.join(split_dob)
        day = join_dob[2:4]
        result = list(map(int, str(day)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)


    def get_life_path(self, num):
        """Returns the computed life path number"""
        split_dob = list(num)
        new_list = []
        for x in split_dob:
            new_list.append(x.replace('-', ''))
        join_list = ''.join(new_list)
        nums = int(join_list)
        result = list(map(int, str(nums)))
        sum_of_list = sum(result)
        result2 = list(map(int, str(sum_of_list)))
        return sum(result2)

    def get_personality(self):
        """ Returns the computed personality number"""
        return self.__personality

    def get_power_name(self):
        """Returns the computed power name number"""
        return self.__power_name

    def get_soul(self):
        """ returns the computed soul number"""
        return self.__soul

