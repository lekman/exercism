# Helper functions
def sum_of(dice:[], expected:int) -> int:
    '''Gets the sum of values for dice that match the given value.
    
    :param dice: list - the different rolled dice values.
    :param expected: int - the expected dice value to match.
    :return: int - number of dice that match the filter value criteria.
    '''
    return sum(i for i in dice if i == expected)

def sorted(dice:[], expected:[]) -> bool:
    '''Sorts the dice then compares the dice to the expected set.
    
    :param dice: list - the different rolled dice values.
    :param expected: int - the expected dice value to match.
    :return: [] - the sorted dice.
    '''
    dice.sort()
    return dice == expected

def full_house_value(dice:[]) -> int:
    '''Determines the full house calcucated value, if valid.
    
    :param dice: list - the different rolled dice values.
    :return: int - sum value of house.
    '''
    three = 0
    two = 0
    for x in range(1, 7):
        if (three == 0 and dice.count(x) == 3):
            three = x
        if (two == 0 and dice.count(x) == 2):
            two = x
    if (three > 0 and two > 0):
        return (three * 3) + (two * 2)
    return 0

# Score categories expressed as Lambda function statements
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: sum_of(x, 1)
TWOS =  lambda x: sum_of(x, 2)
THREES = lambda x: sum_of(x, 3)
FOURS = lambda x: sum_of(x, 4)
FIVES = lambda x: sum_of(x, 5)
SIXES = lambda x: sum_of(x, 6)
FULL_HOUSE = lambda x: full_house_value(x)
LITTLE_STRAIGHT = lambda x: 30 if sorted(x, [1,2,3,4,5]) else 0
FOUR_OF_A_KIND = lambda x: sum(i * 4 for i in set(x) if x.count(i) >= 4)
BIG_STRAIGHT = lambda x: 30 if sorted(x, [2,3,4,5,6]) else 0
CHOICE = sum

# Entry point for unit tests
def score(dice:[], category) -> int:
    '''Scores the dice to a given category.
    
    :param category: int/enum - the category to score against.
    :return: int - sum value of dice by category.
    '''
    # Guard
    if any(not 0 < x < 7 for x in dice):
        raise ValueError("Dice contains invalid numbers.")

    # Execute given lambda
    return category(dice)