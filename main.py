print("Welcome to the tip calculator!")

def tip_calculator(total_bill, number_of_people, percentage):
    percentage = float(percentage / 100)
    individual_bill = total_bill / number_of_people
    total = individual_bill * percentage + individual_bill
    return round(total, 2)

total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("How many people will split the bill? \n"))
percentage = int(input("What percentage of tip would you like to give?\n"))
print("Each person should pay: ", tip_calculator(total_bill, number_of_people, percentage))
