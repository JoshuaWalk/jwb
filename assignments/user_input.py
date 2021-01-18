from datetime import datetime, timedelta

present = datetime.now()

while True:
# GET INPUT FROM USER
    try:
      bd = input("input birthday(YYYY-MM-DD)")
      bdate = datetime.strptime(bd, '%Y-%m-%d')
# VALIDATION
      if bdate > present:
          print("use a date from the past")
          break
    
    except ValueError:
        print("please use the format: YYYY-MM-DD")
# AGE CALCULATION  
    else:
        # VARIABLES
        time_passed = present - bdate
        days = time_passed.days
        minutes = days * 24 * 60 
        seconds = minutes * 60
        weeks = days / 7
        months = days / 30.5

        # USER INPUT
        age_type = input(""" type the following to see your age in: "months" "weeks" "days" "minutes" or "seconds" """).lower()

        # INPUT FUNCTION/VALIDATION
        def age_out(age_type):
            switch={
            "months": f'you are {months} months old',
            "weeks": f'you are {weeks} weeks old',
            "days": f'you are {days} days old',
            "minutes": f'you are {minutes} minutes old',
            "seconds": f'you are {seconds} seconds old'
            }
            print(switch.get(age_type, "invalid answer"))
        # FUNCTION CALL / END OF LOOP
        age_out(age_type)
        break


