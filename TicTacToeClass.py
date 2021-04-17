"""
Building a Tic Tac Toe Class

-check if coordinates are out of bounds
"""


class TicTacToe():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [['_' for i in range(rows)] for j in range(columns)]

    def display_board(self):
        return self.matrix

    def edit_board(self, player, i, j):

        if self.matrix[i][j] == '_':
            self.matrix[i][j] = player
        elif self.matrix[i][j] != '_':
            print(
                'sorry, this spot has already been taken. please choose a different spot'
            )

        display_tt = []
        for row in self.matrix:
            display_tt.append(row)
        return display_tt

    def check_winner_row(self):
        for row in self.matrix:
            if '_' not in row:
                if len(set(row)) == 1:
                    return (f'row winner! Winner is {row[0]}')
            else:
                return ('no winner yet!')

    def check_winner_column(self):
        result = []
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                print(self.matrix[column])

    def check_winner_diagnol(self):
        diagnols = []
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                if (row == column) and self.matrix[row][column] != '_':
                    diagnols.append([row, column])
                    if len(diagnols) == len(self.matrix):
                        return (
                            f'diagnol winner! Winner is {self.matrix[row][column]}'
                        )


tt = TicTacToe(3, 3)
print(tt.display_board())
print(tt.edit_board('x', 0, 0))
print(tt.edit_board('x', 1, 0))
print(tt.edit_board('x', 2, 0))
print(tt.check_winner_row())
print(tt.check_winner_column())
print(tt.check_winner_diagnol())
