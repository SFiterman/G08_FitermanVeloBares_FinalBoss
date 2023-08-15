import pytest 

from src.Ship import Ship

def test_Ship_Mayor20() -> None:
    
    shipA= Ship(40,1) # 40-(1*1,5)=38.5
    assert shipA.is_worth_it() == 38.5
    assert not shipA.is_worth_it() == 88
    
    shipB= Ship(80,5) # 80-(5*1,5)=72.5
    assert shipB.is_worth_it() == 72.5
    assert not shipB.is_worth_it() == 6
    

def test_Cargo_Menor20() -> None:
    shipC= Ship(20,7) # 20-(7*1,5) = 9.5
    with pytest.raises(ValueError, "¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,)"):
        shipC.is_worth_it()
