# 2-3 Land Calculation Program
# 2/28/2021
# Around 10-15 minutes

# Declare Real tractSize, acres
tractSize = 0.0
# Constant
sq_feet_per_acre = 43560


# Display enter the number of sq feet in tract
tractSize = float(input("Enter the number of square feet in the tract: "))

# Equation and answer
acres = tractSize / sq_feet_per_acre
print("The size of that tract is", format(acres, '.3f'), "acres.")

# Im not sure how many decimals are appropriate so I added 3 decimal 
# spots
