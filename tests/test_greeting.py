from greeting import my_name
import pytest

@pytest.fixture
def bob():
    return "My name is: bob"

@pytest.fixture
def sally():
    return "My name is: sally"



def test_bob(bob):
    assert my_name("bob") == bob

def test_sally(sally):
    assert my_name("sally") == sally

def test_my_name3():
    assert my_name("Diego") == "My name is: Diego"

