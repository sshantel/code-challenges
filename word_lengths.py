def word_lengths(sentence):
    """Given a phrase, returns dictionary keyed by word-length,
     with the value for each length being the set of words of that length.
     The output should look like this:
        >>> answer = word_lengths("cute cats chase fuzzy rats")
        >>> sorted(answer.keys())
        [4, 5]
        >>> answer[4] == {'cute', 'cats', 'rats'}
        True
        >>> answer[5] == {'chase', 'fuzzy'}
        True
        >>> answer = word_lengths("Hi, I'm Balloonicorn")
        >>> sorted(answer.keys())
        [3, 12]
        >>> answer[3] == {'Hi,', "I'm"}
        True
        >>> answer[12] == {"Balloonicorn"}
        True
     """
    word_length_dictionary = {}

    split_sentence = sentence.split()
    for word in split_sentence:
        word_length = len(word)
        if word_length in word_length_dictionary:
            word_length_dictionary[word_length].add(word)
        else:
            word_length_dictionary[len(word)] = {word}

    return word_length_dictionary


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if result.failed == 0:
    print("ALL TESTS PASSED")
