# Drug Tests (Farrell Jv 9e 6-11 S21)
# 4/17/2021
# It took me almost an hour because of the issue arising from
# naming the function random :(


# Import Random Module
import random


def main():
    for count in range(1,53):
        
        randomEmployee = randoom()
        
        print("Week", count, ", Employee Number:", randomEmployee)
    
    
def randoom():
    return random.randint(1,30)
    
    
main()
