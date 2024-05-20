print("Welcome to the tip calculator!")

user_bill = input("What was the total bill ($)?: ")
bill_total = float(user_bill)

user_tip_value = input("How much tip would you like to give (10, 12 or 15)?: ")
tip_rate = float(int(user_tip_value) / 100)

people = input("How many people to split the bill?: ")
people_count = int(people)

person_share = round(bill_total * (1 + tip_rate) / people_count, 2)
bill_per_person = "{:.2f}".format(person_share)

print(f"Each person should pay: ${bill_per_person}")
