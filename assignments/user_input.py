from datetime import datetime, timedelta
import math
present = datetime.now()

while True:
    try:
      bd = input("input birthdate (YYYY-MM-DD) \ntype 'stop' to close\n")
      birthday = bd[:4] + '-' + bd[5:7] + '-' + bd[8:]
      if bd == "stop":
          break
      bdate = datetime.strptime(birthday, '%Y-%m-%d')
      if bdate > present:
          print("use a date from the past")
          continue    
    except ValueError:
        print("please use the format: YYYY-MM-DD")

    while True:
        try:
            age_unit = input("Would you like to see your age in...\nmonths, weeks, days, minutes, seconds \ntype 'stop' to exit\n").lower()
            time_passed = present - bdate
            days = time_passed.days
            minutes = math.floor(days * 24 * 60)
            seconds = math.floor(days * 24 *60 * 60)
            weeks = math.floor(days / 7.00)
            months = math.floor(days / 30.50)
            if age_unit == "stop":
                break
            def age_out(age_unit):
                switch={
                "months": f'you are {months} months old\n',
                "weeks": f'you are {weeks} weeks old\n',
                "days": f'you are {days} days old\n',
                "minutes": f'you are {minutes} minutes old\n',
                "seconds": f'you are {seconds} seconds old\n'
                }
                print(switch.get(age_unit, "command not recognized"))
            age_out(age_unit)
            continue
        except ValueError: 
            print("invalid entry") 
    break


