'''
#U: Input is 9 x 9 sudoku board. Output is boolean true or false for if sudoku is
valid

it is valid if (constraints):

- row contains 1-9 WITHOUT duplicates
- column contains 1-9 WITHOUT duplicates
- each of the nine 3 x 3 squares have 1-9 WITHOUT duplicates

I am tasked with determining validity of board

NOTE: Board does not need to be full or be solvable to be valid

#P:
 Initialize 3 sets, one for rows, one for cols, one for squares

nested for loop row and col:
    if row col element is (.):
        continue
    check if board[r][c] is in rows or cols or squares(calculate square position(row // 3, col // 3))
        return false
    add board[r][c] to all sets respectively
#I:
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in square[(r // 3, c // 3)]):
                    return False

                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True


