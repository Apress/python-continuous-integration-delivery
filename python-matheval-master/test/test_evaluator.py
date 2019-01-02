from matheval.evaluator import math_eval

def test_identity():
    assert math_eval(5) == 5, 'identity'

def test_single_element():
    assert math_eval(['+', 5]) == 5, 'single element'

def test_addition():
    assert math_eval(['+', 5, 7]) == 12, 'adding two numbers'

def test_nested():
    assert math_eval(['*', ['+', 5, 4], 2]) == 18
