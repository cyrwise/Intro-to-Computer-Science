# Item Counter (PC 6-4)
# 4/27/2021
# It took me about 20 minutes to complete


def main():

  # Open names.txt
  namesFile = open('names.txt', 'r')

  # priming read
  line = namesFile.readline()

  # Defining the accumulator variable
  namesRead = 0

  # Loop
  while line != '':

    # Defining the line
    nextLine = str(line)
    # Stripping annoying spaces
    nextLine = nextLine.rstrip('\n')

    # The printing machine for names
    print(nextLine)

    # Read next line
    line = namesFile.readline()

    # Accumulator
    namesRead = namesRead + 1

  # Used this to check that accumulator worked,
  # didn't display it though.
  # print(namesRead)

  # Close file
  namesFile.close()

main()
