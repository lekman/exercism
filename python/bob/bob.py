import re

def response(hey:str):
    '''
    Determines the response to a phrase spoken to Bob.
    :param hey:str - the phrase spoken to Bob.
    :return: str - the response from Bob.
    '''
    s = hey.strip()
    shout = re.search("[A-Za-z]", s) != None and s.upper() == s
    question = s.endswith("?")
    silent = re.search("[A-Za-z0-9]", s) == None and not question
    
    if silent:
        return "Fine. Be that way!"
        
    if question:
        if shout:
            return "Calm down, I know what I'm doing!"
        return "Sure."
        
    if shout:
        return "Whoa, chill out!"

    return "Whatever."