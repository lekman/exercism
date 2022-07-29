def is_armstrong_number(number:int) -> bool:
    return sum(
        [int(c) ** len(str(number)) 
            for c in str(number)]
        ) == number