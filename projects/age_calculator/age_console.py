from agecalculator import AgeCalculator

date = input('YYYY/MM/DD\nenter date:')
console = AgeCalculator(date)
console.set_difference()
print(console.age_days(), console.age_hours(), console.age_minutes())





#while True:
    #input('seconds, minutes, hours, days, weeks, or months?')