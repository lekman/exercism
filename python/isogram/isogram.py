import re
def is_isogram(phrase:str):
    s = re.sub("[^a-z]", "", phrase.lower())
    return len(set(s)) == len(s)
