"""
Write a function to turn a phrase into Pig Latin.
Your function will be given a phrase (of one or more space-separated words). There will be no punctuation in it. 
You should turn this into the same phrase in Pig Latin.
>>> pig_latin('porcupines are cute')
'orcupinespay areyay utecay'
>>> pig_latin('give me an apple')
'ivegay emay anyay appleyay'
>>> pig_latin('hello awesome programmer')
'ellohay awesomeyay rogrammerpay'
"""


def pig_latin(phase):
    """Turn a phase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.
    """
    pig_latin_convert = ""
    vowels = "aeiou"

    split_phase = phase.split()

    for word in split_phase:
        if word[0] in vowels:
            word = word + "yay" + " "
            pig_latin_convert += word

        else:
            word = word[1:] + word[0] + "ay" + " "
            pig_latin_convert += word

    return pig_latin_convert.strip()


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if doctest.testmod().failed == 0:
    print("\n✨ ALL TESTS PASSED!\n")
