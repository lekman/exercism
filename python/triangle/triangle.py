def valid(s):
    '''Determine if three list values represent a valid triangle.
    
    Use a lambda function to determine if the triangle is valid (see https://en.wikipedia.org/wiki/Triangle_inequality)
    and that not all sides are of zero length.
    '''
    v = lambda a, b, c, s: a + b >= c and b + c >= a and a + c >= b and set(s) != set([0]) and len(s) == 3
    return v(s[0], s[1], s[2], s)

def equilateral(sides):
    '''Determines if all sides are of equal length. 
    
    In this case, the set length should be '1', meaning all sides are of same length.

    The function 'set' creates a distinct list of values from a regular array/list.
    Measuring the length will give us the amount of distinct values, so a set with 1 value
    means all sides are equal.
    '''
    return valid(sides) and len(set(sides)) == 1
    
def isosceles(sides):
    '''Determines if two or mode sides are of equal length. 
    
    In this case, the set length should be less than '3', meaning that all sides should not be of different length.
    '''
    return valid(sides) and len(set(sides)) < 3

def scalene(sides):
    '''Determines if all sides are of different length. 
    
    In this case, the set length should be '3'.
    '''
    return valid(sides) and len(set(sides)) == 3