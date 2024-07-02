# Total Sales (PC 7-1)
# 5/9/2021
# It took me around 20 minutes to complete


def main():
    
    totalSales = 0
    numbers = [0,0,0,0,0,0,0]
    
    for index in range(7):
        print("Enter the amount of sales for day", index+1)
        sales = int(input(": "))
        numbers[index] = sales
        totalSales += sales
        
    print("The total amount of sales is", totalSales)
        
main()
