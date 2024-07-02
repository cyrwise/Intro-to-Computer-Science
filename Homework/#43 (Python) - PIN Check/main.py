# PIN Check
# 5/9/2021
# It took me around 10-15 minutes to complete, the powerpoint was helpful
# regarding making sure I fully understand the in command after my
# original program.

def main():
    
    # PINS
    workingPins = ["1642", "3501", "0413", "2000", "7811"]
    
    search = input("Enter your PIN number: ")
    
    if search in workingPins:
        print("PIN sucessful; Welcome to the system.")
    else:
        print("Incorrect PIN entered.")
        

main()
