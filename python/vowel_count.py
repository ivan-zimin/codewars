# https://www.codewars.com/kata/54ff3102c1bad923760001f3

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.


def get_count(sentence):
    summ = 0
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            summ += 1
    return summ