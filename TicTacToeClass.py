"""
Building a Tic Tac Toe Class
"""

class TicTacToe():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns 

    def display_board(self):
        matrix = []
        for i in range(self.rows): 
            board = []
            for j in range(self.columns): 
                board.append([0])
        print(board)
        matrix.append(board)
        print(matrix)
        

tt = TicTacToe(3, 3)
print(tt) 
print(tt.display_board) 
print(tt.columns) 