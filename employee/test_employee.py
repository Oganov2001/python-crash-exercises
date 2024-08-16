import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee("Jack", "Jackston", 2000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 7000
    
def test_give_custom_raise(employee):
    employee.give_raise(2000)
    assert employee.salary == 4000
