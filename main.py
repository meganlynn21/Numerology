"""_init__(sName, sDOB)
getName() – returns the subjects name
getBirthdate() – returns the subjects Date of Birth
getAttitude() – returns the computed attitude number
getBirthDay() – returns the computed birthday number
getLifePath() – returns the computed life path number
getPersonality() – returns the computed personality number
getPowerName () – returns the computed power name number
getSoul() – returns the computed soul number
"""

"""Use Numerology.py that will prompt for the user name and birthday 
and then use the Numerology class to get the computed numbers:
•	The two things that are needed to perform a reading is a person’s birth date 
in mm-dd-yyyy format and birth name. 
 The inputted date should be tested to verify that it is entered 
 as a full 8 digit date with dashes or slashes (- or /) as separators.   
•	The inputted name should be populated and not empty.  
•	Call the Numerology class’ __init__ and each function to get the calculated results
•	Output each of the findings to the screen. 
"""

import Numerology

def main():
    name = input("Please input your name: ")
    birthday = input("Please input your birthday in mm-dd-yyyy format: ")

    myNumerology = Numerology.Numerology(name, birthday)
    try:
        birthday.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")