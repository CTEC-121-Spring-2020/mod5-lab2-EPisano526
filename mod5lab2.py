"""
CTEC 121
Esther Pisano   
module 5 lab 2
functions. finger family
"""

""" IPO template
Input(s): family member; daddy, mommy, brother, sister, baby
Process: using functions one can sing whole of finger family song
Output: print finger family song
"""

'''
def name_verse(name):
    print()
    print(name, " finger, ", name, " finger, ")
    print("where are you? Here I am, here I am. How do you do?")

def song():

    name_verse("Daddy")
    name_verse("Mommy")
    name_verse("Brother")
    name_verse("Sister")
    name_verse("Baby")


song()
'''
# practice 2 ages
# Input: Letter for age range
# process: the letter assigned to age
# output: age range


def main(age):

    if age < 2:
        return "I"
    elif age < 13:
        return "C"
    elif age < 18:
        return "T"
    elif age <= 125:
        return "A"
    else:
        return "U"


def testagecode():
    print(main(-1), "expect U:")


testagecode()
