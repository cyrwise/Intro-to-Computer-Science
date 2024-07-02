# Sale Price (ex22)
# 4/16/2021
# It took me around 10-7 minutes, I feel like I got the hang of return
# functions after struggling with the first assignment

# Global constants
DISCOUNT_PERCENTAGE = .20

def main():
    inputRegPrice = float(input("Enter the item's regular price: "))
    salePrice = saleCalculation(inputRegPrice)
    print("The sale price is $", format(salePrice,".2f"))
    
    
def saleCalculation(inputRegPrice):
    salePriceCalc = inputRegPrice - (inputRegPrice * DISCOUNT_PERCENTAGE)
    return salePriceCalc
    
main()
