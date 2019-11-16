def getAvailableLetters(a):
    in_string = str(a)
   
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alp2 = str(alp)
    
    string2 = ""
    
    for x in alp2:
        if x not in in_string:
            string2 += x
    
    return string2
            
            