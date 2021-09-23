import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
        self.position = [5 for x in range(7)]
    
    def move1(self, row, col):
        if self.game_result != "":
            return
        if self.player2 == "":
            return
        self.board[row][col] = self.player1
        self.position[col] = self.position[col]-1
        self.current_turn = 'p2'
        self.remaining_moves = self.remaining_moves-1

        left = col
        right = col
        while left > 0 and self.board[row][left-1] == self.player1:
            left = left-1
        while right < 6 and self.board[row][right+1] == self.player1:
            right = right+1
        if(right - left >= 3):
            self.game_result = 'p1'
            #print('1')
            return


        top = row
        down = row
        while top > 0 and self.board[top-1][col] == self.player1:
            top = top-1
        while down < 5 and self.board[down+1][col] == self.player1:
            down = down+1
        if(down - top >= 3):
            self.game_result = 'p1'
            #print('2')
            return 

        left = col
        right = col
        top = row
        down = row
        while left > 0 and down < 5 and self.board[down+1][left-1] == self.player1:
            left = left-1
            down = down+1
        while right < 6 and top > 0 and self.board[top-1][right+1] == self.player1:
            right = right+1
            top = top-1
        if right-left >= 3:
            self.game_result = 'p1'
            #print('3')
            return

        left = col
        right = col
        top = row
        down = row
        while left > 0 and top > 0 and self.board[top-1][left-1] == self.player1:
            left = left-1
            top = top-1
        while right < 6 and down < 5 and self.board[down+1][right+1] == self.player1:
            right = right+1
            down = down+1
        if right-left >= 3:
            self.game_result = 'p1'
            #print('4')
            return
        
    
    def move2(self, row, col):
        if self.game_result != "":
            return
        if self.player2 == "":
            return
        self.board[row][col] = self.player2
        self.position[col] = self.position[col]-1
        self.current_turn = 'p1'
        self.remaining_moves = self.remaining_moves-1

        left = col
        right = col
        while left > 0 and self.board[row][left-1] == self.player2:
            left = left-1
        while right < 6 and self.board[row][right+1] == self.player2:
            right = right+1
        if(right - left >= 3):
            self.game_result = 'p2'
            #print('5')
            return


        top = row
        down = row
        while top > 0 and self.board[top-1][col] == self.player2:
            top = top-1
        while down < 5 and self.board[down+1][col] == self.player2:
            down = down+1
        if(down - top >= 3):
            self.game_result = 'p2'
            #print('6')
            return 

        left = col
        right = col
        top = row
        down = row
        while left > 0 and down < 5 and self.board[down+1][left-1] == self.player2:
            left = left-1
            down = down+1
        while right < 6 and top > 0 and self.board[top-1][right+1] == self.player2:
            right = right+1
            top = top-1
        if right-left >= 3:
            self.game_result = 'p2'
            #print('7')
            return

        left = col
        right = col
        top = row
        down = row
        while left > 0 and top > 0 and self.board[top-1][left-1] == self.player2:
            left = left-1
            top = top-1
        while right < 6 and down < 5 and self.board[down+1][right+1] == self.player2:
            right = right+1
            down = down+1
        if right-left >= 3:
            self.game_result = 'p2'
            #print('8')
            return
        
    
    

'''
Add Helper functions as needed to handle moves and update board and turns
'''


    
