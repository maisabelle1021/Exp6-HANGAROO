def getGuessedWord(a,b):
    string1=""
    string2 = str(b)
    
    for x in a:
        if x in string2:
            string1 += x
        elif x not in string2:
            string1 += "_"
    
    return string1
        