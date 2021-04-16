"""
Building a Tic Tac Toe Class
"""

class TicTacToe():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns 
        self.matrix = [[0 for i in range(rows)] for j in range(columns)]

    def display_board(self): 
        return self.matrix
tt = TicTacToe(3, 3)
print(tt) 
print(tt.display_board()) 
print(tt.columns)
print(tt.display_board()) 