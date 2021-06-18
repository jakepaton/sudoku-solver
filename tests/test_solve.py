import pytest
from ..src import Sudoku

# testing cases taken from https://www.kaggle.com/bryanpark/sudoku
with open("test_inputs.txt") as file:
    test_inputs = [line.rstrip('\n') for line in file][1:]

with open("test_solutions.txt") as file:
    test_expecteds = [line.rstrip('\n') for line in file][1:]

@pytest.mark.parametrize(('test_input', 'test_expected'), zip(test_inputs, test_expecteds))
def test_solve(test_input, test_expected):
    sudoku = Sudoku(test_input)
    sudoku.solve()
    assert sudoku == test_expected

def test_invalid_input1():
    with pytest.raises(Exception) as e_info:
        sudoku = Sudoku("110000000000000000000000000000000000000000000000000000000000000000000000000000000")

def test_invalid_input2():
    with pytest.raises(Exception) as e_info:
        sudoku = Sudoku("0000000000000000000000000000abc00000000000000000000000000000000000000000000000000")

def test_invalid_input3():
    with pytest.raises(Exception) as e_info:
        sudoku = Sudoku("0000000000000000000000")