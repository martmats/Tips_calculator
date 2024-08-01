print("Welcome to the tip calculator.")
bill = float(input("What is the total bill?"))
tip = int(input("What percentage you would like to give?"))
people = int(input("How many people you would like to split?"))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_tip_total = total_tip + bill
total_amount = total_tip_total / people

total_round = round(total_amount,2)


print(f"Each person should pay {total_round}")
