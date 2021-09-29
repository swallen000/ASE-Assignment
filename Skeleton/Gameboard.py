# import db


class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
        self.position = [5 for x in range(7)]

    def game_draw(self):
        if self.remaining_moves == 0 and self.game_result == '':
            self.game_result = 'draw'
            return True
        if self.game_result == 'draw':
            return True
        return False

    def invalid_turn(self, player):
        if self.current_turn != player:
            return True
        return False

    def game_over(self):
        if self.game_result != "":
            return True
        return False

    def column_full(self, col):
        if self.position[col] < 0:
            return True
        return False

    def player_not_yet_select_color(self):
        if self.player1 == "" or self.player2 == "":
            return True
        return False

    def out_of_board(self, row, col):
        if row > 5 or row < 0 or col > 6 or col < 0:
            return True
        return False

    def move1(self, row, col):
        if self.player_not_yet_select_color() or self.game_draw() \
                or self.invalid_turn('p1') or self.game_over() or \
                self.column_full(col) or self.out_of_board(row, col):
            return False

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
            return True

        top = row
        down = row
        # while top > 0 and self.board[top-1][col] == self.player1:
        #    top = top-1
        while down < 5 and self.board[down+1][col] == self.player1:
            down = down+1
        if(down - top >= 3):
            self.game_result = 'p1'
            return True

        left = col
        right = col
        top = row
        down = row
        while left > 0 and down < 5 and \
                self.board[down+1][left-1] == self.player1:
            left = left-1
            down = down+1
        while right < 6 and top > 0 and \
                self.board[top-1][right+1] == self.player1:
            right = right+1
            top = top-1
        if right-left >= 3:
            self.game_result = 'p1'
            return True

        left = col
        right = col
        top = row
        down = row
        while left > 0 and top > 0 and \
                self.board[top-1][left-1] == self.player1:
            left = left-1
            top = top-1
        while right < 6 and down < 5 and \
                self.board[down+1][right+1] == self.player1:
            right = right+1
            down = down+1
        if right-left >= 3:
            self.game_result = 'p1'
            return True
        self.game_draw()
        return True

    def move2(self, row, col):
        if self.player_not_yet_select_color() or self.game_draw() or \
                self.invalid_turn('p2') or self.game_over() or \
                self.column_full(col) or self.out_of_board(row, col):
            return False

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
            return True

        top = row
        down = row
        # while top > 0 and self.board[top-1][col] == self.player2:
        #    top = top-1
        while down < 5 and self.board[down+1][col] == self.player2:
            down = down+1
        if(down - top >= 3):
            self.game_result = 'p2'
            return True

        left = col
        right = col
        top = row
        down = row
        while left > 0 and down < 5 and \
                self.board[down+1][left-1] == self.player2:
            left = left-1
            down = down+1
        while right < 6 and top > 0 and \
                self.board[top-1][right+1] == self.player2:
            right = right+1
            top = top-1
        if right-left >= 3:
            self.game_result = 'p2'
            return True

        left = col
        right = col
        top = row
        down = row
        while left > 0 and top > 0 and \
                self.board[top-1][left-1] == self.player2:
            left = left-1
            top = top-1
        while right < 6 and down < 5 and \
                self.board[down+1][right+1] == self.player2:
            right = right+1
            down = down+1
        if right-left >= 3:
            self.game_result = 'p2'
            return True
        self.game_draw()
        return True


'''
Add Helper functions as needed to handle moves and update board and turns
'''
