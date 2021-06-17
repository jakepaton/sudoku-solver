""" Sudoku solver using backtracking algorithm """


class Sudoku:
    def __init__(self, sudoku_string):
        self.sudoku = Sudoku.convert_to_2d(sudoku_string)

        # remember positions of starting numbers
        self.permanent = [idx for (idx, chr) in enumerate(sudoku_string) if chr != '0']


    def __repr__(self) -> str:
        return Sudoku.string_repr(self.sudoku)


    def __eq__(self, obj: object) -> bool:
        return Sudoku.string_repr(self.sudoku) == obj


    # string representation of the 2d sudoku
    def string_repr(sudoku):
        return "".join(["".join([str(int) for int in row]) for row in sudoku])


    # converts a sudoku string to a 2d list of ints
    def convert_to_2d(sudoku_string):
        as_2d = [sudoku_string[i*9:(i+1)*9] for i in range(9)]
        as_2d = [[int(chr) for chr in row] for row in as_2d]
        return as_2d    


    def print_2d(self):
        for row in self.sudoku:
            print(row)
        print()
    

    def cols(self):
        return [[row[col_idx] for row in self.sudoku] for col_idx in range(9)]


    def squares(self):
        # centres of squares are at [1, 4, 7] x [1, 4, 7]
        return [[self.sudoku[r+i][c+j] for i in [-1,0,1] for j in [-1,0,1]] for r in [1,4,7] for c in [1,4,7]]


    def contains_duplicates(list):
        non_zero = [int for int in list if int != 0]
        return len(non_zero) != len(set(non_zero))


    # sudoku is valid iff there are no duplicates in rows, columns, or squares
    def is_valid(self):
        for row in self.sudoku:
            if Sudoku.contains_duplicates(row):
                return False
        for col in self.cols():
            if Sudoku.contains_duplicates(col):
                return False
        for square in self.squares():
            if Sudoku.contains_duplicates(square):
                return False
        return True


    def solve(self):
        idx = 0
        while idx != 81:
            # move forwards until we find a non-permanent cell
            while idx in self.permanent:
                idx += 1
            # increment value at this position (idx // 9 == row index; idx % 9 == column index)
            self.sudoku[idx // 9][idx % 9] += 1
            # check we haven't incremented past 9
            if self.sudoku[idx // 9][idx % 9] > 9:
                # we have exhausted the possibilities for this cell so there is an incorrect entry earlier on
                # we set this value to 0 and move backwards to our previous entry
                self.sudoku[idx // 9][idx % 9] = 0
                idx -= 1
                while idx in self.permanent:
                    idx -= 1
                # decrement idx again, as next step will increment it due to sudoku being valid
                idx -= 1
            # if sudoku is valid, we move forward; else we keep incrementing the current cell
            if self.is_valid():
                idx += 1
            if idx < 0:
                raise ValueError("Invalid sudoku; no possible solution")
