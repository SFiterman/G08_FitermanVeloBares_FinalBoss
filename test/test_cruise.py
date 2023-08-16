import pytest 
from src.Cruise import Cruise

def test_Cruise_Mayor20() -> None:
    
    cruceroA= Cruise(230,2000,35) #2000 -(230*2.25 + 35*1,5) = 1430
    assert cruceroA.is_worth_it() == 1430
    assert not cruceroA.is_worth_it() == 130
    
    cruceroB= Cruise(20,1000,65) #1000 -(20*2.25 + 65*1,5) = 1000 - 142,5 = 857,5
    assert cruceroB.is_worth_it() == 857.5
    assert not cruceroB.is_worth_it() == 10
    

def test_Cruise_Menor20() -> None:
    cruceroC = Cruise(20,150,65) #150 -(20*2.25 + 65*1,5) = 150 - 142,5 = 7,5
    with pytest.raises(ValueError):
        cruceroC.is_worth_it()    