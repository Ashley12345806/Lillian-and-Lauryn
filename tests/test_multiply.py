import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply

def test_multiply_first_cycle():
    assert multiply(1, 1) == 1

def test_multiply_second_cycle():
    assert multiply(2, 2) == 4

def test_multiply_third_cycle():
    assert multiply(3, 3) == 9

def test_multiply_fourth_cycle():
    assert multiply(4, 4) == 16