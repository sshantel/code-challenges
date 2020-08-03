"""
Write a function that is given a decimal number and returns the binary number as a string.
>>> dec2bin(6)
'110'
"""


def dec2bin(num):
    """Convert a decimal number to binary representation"""
    result = []
    place = 0

    while place == 0 or num >= 2 ** place:
        print(f"num is {num}")
        if num % (2 ** (place + 1)):
            print(f"(2**(place+1)) is {(2 **(place +1))}")
            num -= 2 ** place
            print(f"result is {result}")
            result.append("1")

        else:
            result.append("0")
        place += 1
    return "".join(reversed(result))


# if __name__ == "__main__":
#     import doctest
# result = doctest.testmod()
# if doctest.testmod().failed == 0:
#     print("\n✨ ALL TESTS PASSED!\n")
