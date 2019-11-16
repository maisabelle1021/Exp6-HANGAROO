def isWordGuessed(a,b):
    secretWord = a
    lettersGuessed = str(b)
    for x in secretWord:
        if x in lettersGuessed:
            output = True
        else:
            output = False
    
    return output