def is_paired(input_string):
    
    op = '' # track opened brackets 
    matched = lambda c, o: (c == '}' and o == '{') or (c == ')' and o == '(') or (c == ']' and o == '[')
    
    for c in input_string:
        if c in '[({': op += c # append open bracket
        if c in '])}': # check that bracket matches
            if len(op) == 0 or not matched(c, op[-1]):
                return False
            op = op[:-1]
  
    return len(op) == 0

print(is_paired("{[]}"))