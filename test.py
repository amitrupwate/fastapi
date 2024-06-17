# test_controllers.py
from controllers import perform_addition

def test_perform_addition():
    assert perform_addition([[1, 2], [3, 4]]) == [3, 7]
