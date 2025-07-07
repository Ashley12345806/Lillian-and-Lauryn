import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply

#First TDD Cycle
def test_multiply_first_cycle():
    # Test multiplying 1 by 1
    #implementing the function
    assert multiply(1, 1) == 1

#Second TDD Cycle
def test_multiply_second_cycle():
    # Test multiplying 2 by 2
    #updating the function to return a * b
    assert multiply(2, 2) == 4

#Third TDD Cycle
def test_multiply_third_cycle():
    # Test multiplying 3 by 3 
    #comfirming the function works for small numbers
    assert multiply(3, 3) == 9

#Fourth TDD Cycle
def test_multiply_fourth_cycle():
    #still a small number, but confirms consistency
    assert multiply(4, 4) == 16

#Fifth TDD Cycle: Test with larger numbers
def test_multiply_fifth_cycle():
    # Test multiplying 23 by 45
    #comfirming the function works for larger numbers
    assert multiply(23, 45) == 1035


    #work done by Lillian Nakato and Lauryn Hope