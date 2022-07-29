import re

pattern = re.compile('^(yt\w*|xr\w*|[aouei]+\w*|squ|qu|[^aouei][^aoueiy]*)')

def pig(word:str) -> str:
    m = re.search(pattern, word)
    i = m.regs[0][1] if m else 0 
    return word if not m else word[i:] + word[0:i] + 'ay'

def translate(text:str) -> str:
    return ' '.join([pig(w) for w in text.split(' ')])