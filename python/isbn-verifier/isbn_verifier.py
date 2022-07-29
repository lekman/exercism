import re
def is_valid(isbn:str):
    # Characters other than X are not allowed
    if len(re.findall("[a-wy-z]", isbn.lower())) > 0:
        return False

    # Strip characters that are not numeric or X
    nums = [n for n in re.sub("[^0-9x]", "", isbn.lower())]
    d = [10 if n == "x" else int(n) for n in nums]

    # String must be 10 characters
    if len(d) != 10:
        return False

    # If X is used then it must only be the last character
    if nums.__contains__("x") and nums.index("x") < 9:
        return False

    # Validate ISBN to formula
    return (d[0] * 10 + d[1] * 9 + d[2] * 8 + d[3] * 7 + d[4] * 6 + d[5] * 5 + d[6] * 4 + d[7] * 3 + d[8] * 2 + d[9] * 1) % 11 == 0