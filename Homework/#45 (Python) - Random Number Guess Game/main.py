# Final, Random Number Guessing Game
# 5/16/2021
# It took me: Around 20 minutes or more to complete.

import random

def main():
    
    guessTwo = 0
    realnum = random.randint(1,100)
    
    print("I am thinking of a number between 1 and 100.")
    guess = int(input("Can you guess what it is? Enter your guess. "))
    
    while realnum != guessTwo:
        
        if guess > realnum:
            print(guess, "is too high. Try a smaller number: ")
            guess = int(input(""))
            
        elif guess < realnum:
            print(guess, "is too low. Try a larger number: ")
            guess = int(input(""))
            
        else:
            print("Congratulations! You figured out the number (", realnum, ").")
            guessTwo = guess
    
    
    
main()
