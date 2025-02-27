#DAY 2 PROJECT
print("Hello Mr. IK, Welcome to the Tip Calculator!")
bill = float(input("What is the total bill?\nN"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = bill *(1+ tip/100)
bill_per_person = bill_with_tip/people
final_bill = round(bill_per_person,2)
print(f"Each person should pay: N{final_bill}")

