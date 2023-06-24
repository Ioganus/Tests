import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator
        
    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2
    
    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1,1) == 3
    
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)
    
    def teardown_method(self):
        print ('Выполнение метода TearDown')