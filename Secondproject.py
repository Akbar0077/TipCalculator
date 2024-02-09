print("Welcome to the tip calculator.")
bill=float(input("What was the total bill?$"))
tip=int(input("What tip would you like to give?"))
numbers=int(input("How many people to split the bill?"))
result = bill + tip
total_bill=result/numbers
print("Each person should pay: $", total_bill)
