# Average of Numbers (PC 6-6)
# 4/27/2021
# It took me about 20 minutes to complete. This was one was fun


def main():

    lineNumber = 0
    totalAmount = 0

    numbersFile = open('numbers.txt', 'r')

    # Loop to read all lines
    for line in numbersFile:
    
      amount = float(line)

      print(amount)

      lineNumber = lineNumber + 1

      # Accumulator for total
      totalAmount = totalAmount + amount

      # Accumulator for each line
      # print(lineNumber)

    totalAmount = totalAmount / lineNumber
    print("The average is", format(totalAmount, ',.2f'))

    numbersFile.close()

main()
