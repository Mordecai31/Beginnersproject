print("Welcome to DigIT Organization")
a = input("Input the Employee's Name: ")
hours_worked = input("Enter the amount of hours:")
hourly_wage = 500

def wagesalary():
    if float(hours_worked) > 60:
        print("Maximum work hour for a week is 60 hr(s).")

    if float(hours_worked) <= 40:
        wage = float(hours_worked) * 500
        print(f"Your name is {a} and you have worked for {hours_worked} hours and receive a total amount of ${wage}")


    elif 40 < float(hours_worked) <= 60:
        Extra_hours = float(hours_worked)-40
        regular_rate = 40*500
        bonus_rate = Extra_hours*1000
        wage = float(regular_rate)+float(bonus_rate)
        print(f"Your name is {a} and you have worked for {hours_worked} hours that awarded you to receive a bonus ${bonus_rate} and receive a total amount of ${wage}")

wagesalary()
