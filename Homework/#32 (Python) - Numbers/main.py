# Numbers (Farrell 8th J 3-4)
# 4/10/2021
# It took about: 15 minutes, it does not exactly match sample run
# though it completes the same task

def main():
    numInputOne = float(input("Enter a number: "))
    numInputTwo = float(input("Enter another number: "))
    displayTwiceTheNumber(numInputOne, numInputTwo)
    
def displayTwiceTheNumber(numOneTwiced, numTwoTwiced):
    final_NumOneTwiced = numOneTwiced * 2
    final_NumTwoTwiced = numTwoTwiced * 2
    print(numOneTwiced, "times 2 is", final_NumOneTwiced)
    print(numTwoTwiced, "times 2 is", final_NumTwoTwiced)
    displayNumberSquared(numOneTwiced, numTwoTwiced)
    
def displayNumberSquared(numOneSquared, numTwoSquared):
    final_NumOneSquared = numOneSquared * numOneSquared
    final_NumTwoSquared = numTwoSquared * numTwoSquared
    print(numOneSquared, "squared is", final_NumOneSquared)
    print(numTwoSquared, "squared is", final_NumTwoSquared)
    
main()
