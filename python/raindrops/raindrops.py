def convert(number:int) -> str:
    '''Converts a number into a raindrop sound.
    :param unmber:str - the number to convert.
    :return: str - the raindrop sound.
    '''
    
    sound = ""
    
    # if number has 3 as a factor, add 'Pling' to the result.
    if number % 3 == 0:
        sound += "Pling"

    # if number has 5 as a factor, add 'Plang' to the result.
    if number % 5 == 0:
        sound += "Plang"

    # if number has 7 as a factor, add 'Plong' to the result.
    if number % 7 == 0:
        sound += "Plong"

    if len(sound) > 0:
        return sound
        
    # if number does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
    return str(number)