# Golf Scores (PC 6-10) PROGRAM 2
# 4/27/2021
# I don't know how long it took me, but I understand better now.
# I was having troubles with how to store my lines in variables
# and display them, but looking at your program it looks a lot
# more simple than I had thought.

def main():
    # Local variables
    line = ''
    name = ''
    golf_score = 0
    num_players = 0

    # Open golf.txt for reading
    golfTxt = open('golf.txt', 'r')

    # declaring the accumulators
    scores = 0
    rounds = 0
  
    # Read first name
    name = golfTxt.readline()

    # The priming read loop
    while name != '':
        # I think that it first reads name from beginning, then makes the second line known as the score
        golf_score = int(golfTxt.readline())

        # this strips and separates to the next line
        name = name.rstrip('\n')

        # Display data with one line space between the data 
        # for every two players 
        scores += 1
        rounds += golf_score 
        print ('Name:', name)
        print ('Golf Score:', golf_score)

        # Read next name which then repeated the process
        name = golfTxt.readline()

    # I added the \n since I realized it separated next line
    print ("\nNumber of Golfers:", scores)
    print ("Average Score:", (rounds/scores))

    # Closing the file
    golfTxt.close()

# Calling main
main()
