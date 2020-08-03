"""
Given two lists. concatenate them (that is, combine them into a single list).

>>> concat_lists([1, 2], [3, 4])
[1, 2, 3, 4]

>>> concat_lists([], [1, 2])
[1, 2]

>>> concat_lists([1, 2], [])
[1, 2]

>>> concat_lists([], [])
[]

"""


def concat_lists(list1, list2):
    """Combine lists."""
    return list1 + list2


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if doctest.testmod().failed == 0:
    print("\n✨ ALL TESTS PASSED!\n")
