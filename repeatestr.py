def mostRepeatedChar(str):
    h = {} 
    for ch in str:
        if ch in h:
            return ch;
        else:
            h[ch] = 0
    return '\0'
 
print("most repeated char is:")
print(mostRepeatedChar("helloworld"))
