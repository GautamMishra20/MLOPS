import pytest
from app import sq, cube, fifth_power

def test_sq():
    assert sq(2) == 4
    assert sq(3) == 9
    assert sq(-4) == 16

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(-2) == -8

def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(-2) == -32

def test_zero():
    assert sq(0) == 0
    assert cube(0) == 0
    assert fifth_power(0) == 0

def test_invalid_input():
    with pytest.raises(TypeError):
        sq("string")