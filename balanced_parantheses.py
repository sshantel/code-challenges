def has_balanced_parens(phrase):
    """
    Given a string, return True or False depending on whether that string has balanced parentheses.
    For the purposes of this problem, you only need to worry about parentheses (( and )), not other opening-and-closing marks, like curly brackets, 
    square brackets, or angle brackets.
    >>> has_balanced_parens("()")
    True
    >>> has_balanced_parens("(Oh Noes!)(")
    False
    >>> has_balanced_parens("((There's a bonus open paren here.)")
    False
    >>> has_balanced_parens(")")
    False
    >>> has_balanced_parens("(")
    False
    >>> has_balanced_parens("(This has (too many closes.) ) )")
    False
    >>> has_balanced_parens("Hey...there are no parens here!")
    True
    """
    parentheses = 0

    for char in phrase:
        if char == "(":
            parentheses += 1
        elif char == ")":
            parentheses -= 1
            if parentheses < 0:
                return False

    if parentheses > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
