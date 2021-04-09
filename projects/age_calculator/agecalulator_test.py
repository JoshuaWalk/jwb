import pytest
from agecalculator import *
from params import *

# UNUSED FIXTURES

@pytest.fixture
def date_one():
    birthday = AgeCalculator('1997-04-08', '2021-04-07')
    birthday.set_difference()
    return birthday

@pytest.fixture
def date_two():
    date = AgeCalculator('1932-08-16', '2021-04-09')
    date.set_difference()
    return date

@pytest.fixture
def date_old():
    date = AgeCalculator('1321-11-09', '2021-04-09')
    date.set_difference()
    return date

@pytest.fixture
def age_future():
    date = AgeCalculator('2055-02-28', '2021-04-07')
    date.set_difference()
    return date

# TESTS

@pytest.mark.parametrize("a, b, out", dates_seconds)
def test_seconds(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_seconds() == out

@pytest.mark.parametrize("a, b, out", dates_minutes)
def test_minutes(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_minutes() == out

@pytest.mark.parametrize("a, b, out", dates_hours)
def test_hours(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_hours() == out

@pytest.mark.parametrize("a, b, out", dates_days)
def test_days(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_days() == out

@pytest.mark.parametrize("a, b, out", dates_weeks)
def test_weeks(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_weeks() == out

@pytest.mark.parametrize("a, b, out", dates_months)
def test_months(a, b, out):
    calc = AgeCalculator(a, b)
    calc.set_difference()
    assert calc.age_months() == out


