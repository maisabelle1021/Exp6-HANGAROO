def Hangaroo():
    import random
    wordList=["jojo","joseph","jotaro","dio","caesar","jolyne","johnny","giorno","stand","hamon"]
    secretWord=random.choice(wordList)
    lettersGuessed = ""
    counter=0

    print("Hello! Are you ready to play a game?")
    print("[1]Yes     [2]No" )
    num = input( )
    d = int(num)
    if d == 1:
        for i in range(0,5,1):
            while counter < 5:
                print("Guess a letter: ")
                txt = input( )
                s = txt.lower()
                print(" ")
                lettersGuessed += s
                print(getGuessedWord(secretWord,lettersGuessed))
                print("LETTERS AVAILABLE: ", getAvailableLetters(lettersGuessed))
                print(" ")
                counter += 1
                if counter == 5:
                    break
                else:
                    continue
        
        f = isWordGuessed(secretWord,lettersGuessed)
                
        if f==True:
            print("Congratulations! You won the game!")
        else:
            print("Oops, looks like you weren't able to guess the word!")
            print("The word was", "'",secretWord,"'")
            
    elif d == 2:
        print("No? Goodbye then!")
    else:
        print("ERROR")

            
    
    
    
        
        
        
        