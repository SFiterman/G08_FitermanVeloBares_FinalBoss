from src.Cargo import cargo
import pytest

def test_Cargo_Mayor20() -> None:
    
    cargoA= cargo(10,1,100,5) #100-(5*1.5+3.5*10)=57.5
    assert cargoA.is_worth_it() == 57.5
    assert not cargoA.is_worth_it() == 890
    
    cargoB= cargo(15,2,65,2) #65-(2*1.5+3.5*15)= 27
    assert cargoB.is_worth_it() == 27
    assert not cargoB.is_worth_it() == 876
    

def test_Cargo_Menor20() -> None:
    cargoC= cargo(10,1,50,9) #50-(9*1.5+3.5*10)=  1.7
    with pytest.raises(ValueError, "¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,)"):
        cargoC.is_worth_it()
