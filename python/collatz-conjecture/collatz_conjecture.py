def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    loops = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else (number * 3) + 1
        loops += 1
        
    return loops