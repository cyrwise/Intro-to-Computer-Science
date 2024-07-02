# Salesperson Pay with Commission (ex23)
# 4/16/2021
# It took me 10-15 minutes to complete

def main():
    
    # Ask for monthly sales
    monthlySales = float(input("Enter the monthly sales: "))
    
    # Pass to other function to calculate commission rate
    commission = calculator(monthlySales)
    
    # Give output
    print("The pay is $", format(commission,".2f"))
    
def calculator(monthlySales):
    if monthlySales<10000:
        commissionCalc = monthlySales * .10
        return commissionCalc
    elif monthlySales<=14999:
        commissionCalc = monthlySales * .12
        return commissionCalc
    elif monthlySales<=17999:
        commissionCalc = monthlySales * .14
        return commissionCalc
    elif monthlySales<=21999:
        commissionCalc = monthlySales * .16
        return commissionCalc
    elif monthlySales>=22000:
        commissionCalc = monthlySales * .18
        return commissionCalc
        
        
# Call the main function
main()
