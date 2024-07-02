# How Much Insurance? (5-3)
# 4/8/2021
# It took around 10-15 minutes because I tried to add commas to
# final product but I am not sure how, unfortunately I was deceived by stack
# overflow in the process

def main():
    # input
    replAmount = float(input("Enter the replacement amount: "))
    
    # Matheemateeks
    minInsurance = replAmount * 0.80
    
    # Output
    print("Percent insured: 80")
    print("Minimum Insurance amount is: ", format(minInsurance, ".2f"))
    
main()
