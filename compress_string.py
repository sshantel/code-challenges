"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats. If a character appears once, it should not be followed by a number.
The function should handle letters, whitespace, and punctuation.

>>> compress('aabbaabb')
'a2b2a2b2' 
>>> compress('abc')
'abc' 
>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""

    compressed = []
    current = ""
    count = 0

    for char in string:
        if char != current:
            compressed.append(current)

            if count > 1:
                compressed.append(str(int(count)))

            current = char
            count = 0

        count += 1

    compressed.append(current)
    if count > 1:
        compressed.append(str(int(count)))

    return "".join(compressed)


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if doctest.testmod().failed == 0:
    print("\n✨ ALL TESTS PASSED!\n")
