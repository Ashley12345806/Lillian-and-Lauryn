import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fibonacci import fibonacci
def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_4():
    assert fibonacci(4) == 3