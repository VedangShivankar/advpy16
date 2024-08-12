import mathlib

def test_calc_total():
    total = mathlib.calc_square(4,5)
    assert total == 9

def test_clac_multiply():
    result =  mathlib.calc_multipy(10,3)
    assert result == 30 