# import pytest
from myapplication import functions

def test_add_some_materials(): 
    
    dict={}
    result = functions.adding_materials(dict,"shekar","10")
    assert result == {'shekar': 10}

def test_difining_cookie():
    dict={}
    result = functions.defining_cookies(dict,"khameyi","10000",2,['define', 'suit', 'khameyi', '10000', 'shekar', '10', 'namak', '5'])
    assert result == {'khameyi': {'price': 10000, 'shekar': 10, 'namak': 5}}