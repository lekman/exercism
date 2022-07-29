def rotate(text: str, key: int):
    a = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    key = key % 26
    for c in text:
        try:
            i = (a.index(c.lower()) + key) % 26
            x = a[i:i+1] 
            out += x.upper() if c.isupper() else x
        except:
            out += c
    return out
