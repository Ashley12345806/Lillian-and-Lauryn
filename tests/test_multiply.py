#work done by Lillian Nakato and Lauryn Hope
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply

#First TDD Cycle
def test_multiply_first_cycle():
    #implementing the function
    assert multiply(1, 1) == 1

#Second TDD Cycle
def test_multiply_second_cycle():
    #updating the function to return a * b
    assert multiply(2, 2) == 4

#Third TDD Cycle
def test_multiply_third_cycle():
    #comfirming the function works for small numbers
    assert multiply(3, 3) == 9

#Fourth TDD Cycle
def test_multiply_fourth_cycle():
    assert multiply(4, 4) == 16

#Fifth TDD Cycle
 # ensuring the function works correctly for larger numbers
def test_multiply_fifth_cycle():
    assert multiply(23, 45) == 1035

def test_multiply_six_cycle():
    assert multiply(-10, -10) == 100

def test_multiply_cycle():
    assert multiply(-10, 10) == -100
 