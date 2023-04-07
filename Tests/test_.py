# import pytest
from myapplication.functions import adding_materials

def test_add_some_materials(): 
    
    dict={}
    result = adding_materials(dict,"shekar","10")
    assert result == {'shekar': 10}
