# Random Number File Writer (PC 6-7)
# 4/27/2021
# It took me about 15 minutes, I wasn't sure if
# I needed to print the numbers but I decided not to
# since I didn't see it ask to do so in the assignment prompt

import random

def main():

  numOfNums = int(input("How many random numbers should be written?: "))

  randFile = open('randomnumbers.txt', 'w')

  for count in range(1, numOfNums + 1):

    number = random.randint(1,500)

    randFile.write(str(number) + '\n')

  randFile.close()
  print(numOfNums, "numbers generated in randomnumbers.txt")

main()
