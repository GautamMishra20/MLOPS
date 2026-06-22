import pytest
from app import sq, cube, fifth_power

def test_sq():
    assert sq(2) == 4 , "Test Failed: Square of 2 should be 4"
    assert sq(3) == 9 , "Test Failed: Square of 3 should be 9"

def test_cube():
    assert sq(2) == 8 , "Test Failed: Square of 2 should be 8"
    assert sq(3) == 27 , "Test Failed: Square of 3 should be 27"

def test_fifth_power():
    assert sq(2) == 32 , "Test Failed: Square of 2 should be 32"
    assert sq(3) == 243 , "Test Failed: Square of 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        sq("string") 