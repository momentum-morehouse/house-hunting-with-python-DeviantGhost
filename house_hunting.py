# Write your code here
total_cost = float(input("What is the cost of your dream home? "))

portion_down_payment = (total_cost * 0.25)

r = 0.04

annual_salary = float(input("What is your annual salary? "))

portion_saved = float(input("How much of your monthly salary do you want to save? "))*(annual_salary/12)

def invest_savings(current_savings):
    return float(current_savings*r)/12

def timeRequired(portion_saved, portion_down_payment):
    current_savings = 0
    num_Months = 0
    while current_savings < portion_down_payment:
        current_savings += invest_savings(current_savings)
        current_savings += portion_saved
        num_Months += 1

    return print("It would require " + str(num_Months) + " months to save $" + str(portion_down_payment))

timeRequired(portion_saved, portion_down_payment)

