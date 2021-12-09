# https://www.codewars.com/kata/52fba66badcd10859f00097e

import re

def disemvowel(string):
    result = re.sub(r'[aeiouAEIOU]', '', string)
    return result

print(disemvowel('Hello'))


# better solution
"""
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
"""