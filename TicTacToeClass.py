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

    def edit_board(self, player, i, j): 
        self.matrix[i][j] = player
        return self.matrix

tt = TicTacToe(3, 3) 
print(tt.display_board())  
tt.edit_board(0,0) 
print(tt.edit_board('x',0,0))
print(tt.display_board())