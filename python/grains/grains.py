def square(number:int) -> int:
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64") 
    return 2 ** (number - 1)

def total():
    return sum(square(x+1) for x in range(64))