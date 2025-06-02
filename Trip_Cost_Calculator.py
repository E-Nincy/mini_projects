# Trip Cost Calculator
# This is a small project to get yourself warmed up and keep training your newly found skills in collecting user input and formatting strings.

# Create a Python script that asks a user questions in the command line. The script should follow the outlined specifications.

# Specifications
# Receive the following arguments from the user:

# 1.Kilometers to drive
# 2. Liters-per-kilometer usage of the car
# 3. Price per liter of fuel  

# Calculate the cost of the trip and display it to the user in the console. 
# Apply some of the string formatting tricks that you learned about in this course section.

kilometers = float(input("Enter the total of Kilometers to drive:"))
liters_per_km = float(input("Enter the liters per kilometer your car uses: "))
price_per_liter = float(input("Enter the price per liter of fuel: "))

total_liters = kilometers * liters_per_km
total_cost = total_liters * price_per_liter

print(f"The total cost of the trip is: €{total_cost:.2f}")