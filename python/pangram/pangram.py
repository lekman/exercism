import re
def is_pangram(sentence):
    '''Determines is a sentence is a pangram.
    :param sentence: str - the sentence to test.
    :return: bool - true if a pangram, otherwise false.

    A pangram is a sentence that uses all letters of the English alphabet at least once.
    A famous pangram sentence is "the quick brown fox jumps over the lazy dog".
    '''
    return len( # Measure number of unique letters
        set( # Split into unique letters
            re.sub( # User RegEx library to filter input
                '[^A-Za-z]*', '', # Match non-alpha characters
                sentence.lower())) # Search original string, but in lower-case
            ) == 26 # NUmber of letters should be 26, i.e entire English alphabet