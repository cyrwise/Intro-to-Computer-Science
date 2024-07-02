# Lottery Number Generator (PC 7-2)
# 5/9/2021
# It took me around 20 minutes as well, I looked at the video to be sure
# though I felt like what I did on my own worked. I added some of their
# suggestions cause it made my code look cleaner.

import random

def main():
    numbers = [0,0,0,0,0,0,0]
    
    for index in range(7):
        numbers[index] = random.randint(0,9)
        
    
    print("Your lottery numbers are:")
    
    for index in range(7):
        print(numbers[index], end="")
    print()
    
main()
