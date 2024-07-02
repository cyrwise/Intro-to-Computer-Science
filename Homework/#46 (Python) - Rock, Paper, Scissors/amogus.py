# Final, Rock Paper Scissors
# 5/16/2021
# It took me: about an hour since I had so much fun with our final
# program of the class. Thanks for being a great teacher and having
# fun video lessons for your class, farewell and take care! :)

import random

def main():
    
    y = "y"
    n = "n"
    y2 = "Y"
    n2 = "N"
    
    
    secretEnding = str(input('Do you happen to be REDACTED?' \
    ' "Y" for yes, "N" for no. '))
    passwordAttempt = ''
    
    
    if secretEnding == n or secretEnding == n2:
        print("")
        print("Continuing the program as normal...")
        print("")
    elif secretEnding == y or secretEnding == y2:
        passwordAttempt = str(input("Enter the secret passcode" \
        " in this program: "))
        # not so secret, its right here:
        password = "amongus"
        
        if passwordAttempt == password:
            print("")
            print("You have received a free win! Loading new game...")
            print("")
        else:
            print("")
            print("You are an impostor! Quite SUS!")
            print("")
    
    else:
        print("")
        print("Not an applicable answer, you have lost your chance.")
        print("")
        
        
    playAgain = 1
    
    while playAgain != 0:
    
        canContinue = 0
    
        print("1 = Rock; 2 = Paper; 3 = Scissors")
        userChoice = int(input("Input the integer for your choice: "))
    
        print("")
    
        while canContinue != 1:
        
            if userChoice<1:
            
                userChoice = int(input("Invalid integer entered. Try again: "))
            
            if userChoice>3:
            
                userChoice = int(input("Invalid integer entered. Try again: "))
            
            else:
                canContinue = 1
    
        if userChoice==1:
            print("User: Rock")
        
        elif userChoice==2:
            print("User: Paper")
        else:
            print("User: Scissors")
    
        finalResult = theBattle(userChoice)
        
        if finalResult==0:
            print("CPU wins!")
        if finalResult==1:
            print("User wins!")
        if finalResult==2:
            print("It's a tie!")
            
        print("")
        
        while canContinue != 2:
        
            
            userPlayAgain = str(input('Would you like to play again?' \
            ' "Y" for yes, "N" for no. '))
            
            if userPlayAgain == y or userPlayAgain == y2 \
            or userPlayAgain == n or userPlayAgain == n2:
                canContinue = 2
            else:
                print("Error: Input is neither Y nor N.")
                    
            
        if userPlayAgain == n or userPlayAgain == n2:
            print("")
            print("Exiting program...")
            playAgain = 0
        else:
            print("")
            print("Loading new game...")
            print("")
            

 
    

def theBattle(usersInteger):
    
    cw = 0      #CPU win
    uw = 1      #user win
    bt = 2      #both win
    
    botsInteger = random.randint(1,3)
    # rock = 1, paper = 2, scissors = 3
    
    # Display bot choice
    
    if botsInteger==1:
        print("CPU: Rock")
    elif botsInteger==2:
        print("CPU: Paper")
    else:
        print("CPU: Scissors")
    
    # The battle
    
    # if bot has rock
    if botsInteger==1 and usersInteger==1:
        return bt
    elif botsInteger==1 and usersInteger==2:
        return uw
    elif botsInteger==1 and usersInteger==3:
        return cw
    
    # if bot has paper
    elif botsInteger==2 and usersInteger==1:
        return cw
    elif botsInteger==2 and usersInteger==2:
        return bt
    elif botsInteger==2 and usersInteger==3:
        return uw
        
    # if bot has scissors
    elif botsInteger==3 and usersInteger==1:
        return uw
    elif botsInteger==3 and usersInteger==2:
        return cw
    elif botsInteger==3 and usersInteger==3:
        return bt
    
    
main()
