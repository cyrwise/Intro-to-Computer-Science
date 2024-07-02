# Bookstore Credit (Farrell 8th J 3-6)
# 4/10/2021
# It took around: 15 minutes. I forgot a parenthesis at the end of
# the statement regarding gpaInput which had me troubleshooting for
# a while as it told me line 15 was specifically wrong. I also tried
# to remove spaces with the final print command but i am not sure how.


def main():
    nameInput = input("Enter your first name: ")
    gpaInput = float(input("Enter your GPA: "))
    calcCredit(nameInput, gpaInput)
    
def calcCredit(nameOutput, gpaCalc):
    creditFinal = gpaCalc * 50
    print(nameOutput,", your GPA is",format(gpaCalc, ".1f"), \
    ", so your credit is $",format(creditFinal, ".1f"),"!")
    
main()
