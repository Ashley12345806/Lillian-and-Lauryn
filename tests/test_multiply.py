import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply

def test_multiply_first_cycle():
    assert multiply(1, 1) == 1