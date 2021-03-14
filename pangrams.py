"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example
The string contains all letters in the English alphabet, so return pangram.

Function Description
Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):
string s: a string to test
Returns
string: either pangram or not pangram
Input Format

A single line with string s.
"""

def pangrams(s):
    ascii_set = set()
    for letter in s.lower():
        if letter not in ascii_set and letter.isalpha():
            ascii_set.add(letter) 
    print(ascii_set)
    if len(ascii_set) == 26:
        return "pangram"
    else:
        return "not pangram"

print(pangrams('We promptly judged antique ivory buckles for the next prize'))