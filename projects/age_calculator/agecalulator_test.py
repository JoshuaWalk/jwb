import pytest
from agecalculator import *

@pytest.fixture
def date_one():
    birthday = AgeCalculator('1997-04-08', '2021-04-07')
    birthday.set_difference()
    return birthday

@pytest.fixture
def date_two():
    return AgeCalculator('1932-08-16', '2021-04-07')

@pytest.fixture
def date_old_one():
    return AgeCalculator('1321-11-09', '2021-04-07')

@pytest.fixture
def age_future_one():
    return AgeCalculator('2055-02-28', '2021-04-07')

@pytest.mark.birthday
def test_days_one(age_one):
    assert age_one.age_days() == ("days", 8765)