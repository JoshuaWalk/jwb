from datetime import datetime, timedelta
import math

def getAge(birthdate):
    present = datetime.now()
    bdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = present - bdate
    if age.days < 0:
        print('are you from the future?')
    return age.days

def getAgeSeconds(age):
    return age * 24 * 60 * 60

def getAgeMinutes(age):
    return age * 24 * 60

def getAgeHours(age):
    return age * 24

def getAgeWeeks(age):
    return math.floor(age / 7)

def getAgeMonths(age):
    return math.floor(age / 30.5)


getAge('1997-04-08')
getAge('2021-05-05')



