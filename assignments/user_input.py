from datetime import datetime, timedelta
# ask for birthdate and validate
    # date can't be in the future
present = datetime.now()

while True:
    try:
      bd = input("input birthday(YYYY-MM-DD)")
      bdate = datetime.strptime(bd, '%Y-%m-%d')
    
    except ValueError:
        print("please use the format: YYYY-MM-DD")     
    else:
        break

if bdate > present:
            print("You were not born in the future")

# user chooses to see age in months, weeks, days, minutes, or seconds
    # returns correct age

time_passed = present - bdate

age_type = input(""" type the following to see your age in: "months" "weeks" "days" "minutes" or "seconds" """)

days = time_passed.days
minutes = days * 24 * 60 
seconds = minutes * 60
weeks = days / 7
months = days / 30.5

print("D: ", days, "W: ", weeks, "M: ", months, "m", minutes, "s", seconds)
def age_out(age_type):
        switch={
            "months": f'you are {months} months old',
            "weeks": f'you are {weeks} weeks old',
            "days": f'you are {days} days old',
            "minutes": f'you are {minutes} minutes old',
            "seconds": f'you are {seconds} seconds old'
        }
        print(switch.get(age_type, "invalid answer"))
age_out(age_type)