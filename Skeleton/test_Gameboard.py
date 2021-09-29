import unittest
from Gameboard import Gameboard
import random


class Test_TestGameboard(unittest.TestCase):

    def test_init_status(self):
        game = Gameboard()
        self.assertEqual(game.player1, "")
        self.assertEqual(game.player2, "")
        self.assertEqual(game.board, [[0 for x in range(7)] for y in range(6)])
        self.assertEqual(game.game_result,  "")
        self.assertEqual(game.current_turn, 'p1')
        self.assertEqual(game.remaining_moves, 42)
        self.assertEqual(game.position, [5 for x in range(7)])

    def test_happy_move(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # player1 move
        col1 = random.randint(0, 6)
        row1 = game.position[col1]
        self.assertEqual(game.move1(row1, col1), True)

        # test after player1 move
        self.assertEqual(game.board[row1][col1], 'red')
        self.assertEqual(game.current_turn, 'p2')
        self.assertEqual(game.game_result, '')
        self.assertEqual(game.remaining_moves, 41)
        self.assertEqual(game.position[col1], row1-1)

        # player2 move
        col2 = random.randint(0, 6)
        row2 = game.position[col2]
        self.assertEqual(game.move2(row2, col2), True)

        # test after player2 move
        self.assertEqual(game.board[row2][col2], 'yellow')
        self.assertEqual(game.current_turn, 'p1')
        self.assertEqual(game.game_result, '')
        self.assertEqual(game.remaining_moves, 40)
        self.assertEqual(game.position[col2], row2-1)

    def test_not_p1_turn(self):
        game = Gameboard()
        game.player1 = 'red'
        game.current_turn = 'p2'
        self.assertEqual(game.invalid_turn('p1'), True)

        # invalid move for player1, the board should be the same
        self.assertEqual(game.move1(game.position[0], 0), False)
        self.assertEqual(game.board[5][0], 0)

    def test_not_p2_turn(self):
        game = Gameboard()
        game.current_turn = 'p1'
        self.assertEqual(game.invalid_turn('p2'), True)

        # invalid move for player2, the board should be the same
        self.assertEqual(game.move2(game.position[0], 0), False)
        self.assertEqual(game.board[5][0], 0)

    def test_winner_already_exist(self):
        game = Gameboard()
        # test if winner is p1
        game.game_result = 'p1'
        self.assertEqual(game.game_over(), True)

        # test if winner is p2
        game.game_result = 'p2'
        self.assertEqual(game.game_over(), True)

    def test_draw_by_moves(self):
        game = Gameboard()
        game.remaining_moves = 0
        self.assertEqual(game.game_draw(), True)
        self.assertEqual(game.game_result, 'draw')

        game = Gameboard()
        game.remaining_moves = 1
        self.assertEqual(game.game_draw(), False)
        self.assertEqual(game.game_result, '')

    def test_draw_by_board(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.board = [
            ['', 'red', 'yellow', 'yellow', 'red', 'red', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red'],
            ['red', 'red', 'yellow', 'yellow', 'red', 'red', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red'],
            ['red', 'red', 'yellow', 'yellow', 'red', 'red', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red']
        ]

        # game should be draw after p1's move
        game.remaining_moves = 1
        game.current_turn = 'p1'
        self.assertEqual(game.move1(0, 0), True)
        self.assertEqual(game.game_draw(), True)
        self.assertEqual(game.game_result, 'draw')

        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.board = [
            ['', 'red', 'red', 'red', 'yellow', 'yellow', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red'],
            ['red', 'red', 'yellow', 'yellow', 'red', 'red', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red'],
            ['red', 'red', 'yellow', 'yellow', 'red', 'red', 'yellow'],
            ['yellow', 'yellow', 'red', 'red', 'yellow', 'yellow', 'red']
        ]

        # p1 should win after fill the empty place
        game.remaining_moves = 1
        game.current_turn = 'p1'
        self.assertEqual(game.move1(0, 0), True)
        self.assertEqual(game.game_draw(), False)
        self.assertEqual(game.game_result, 'p1')

    def test_current_column_full(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[0], 0), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[0], 0), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[0], 0), True)

        # column 0 should be full now
        self.assertEqual(game.column_full(0), True)
        # other columns should be fine
        self.assertEqual(game.column_full(1), False)
        self.assertEqual(game.column_full(2), False)
        self.assertEqual(game.column_full(3), False)
        self.assertEqual(game.column_full(4), False)
        self.assertEqual(game.column_full(5), False)
        self.assertEqual(game.column_full(6), False)

    def test_winning_move_horizontal_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[0], 0), True)
        self.assertEqual(game.move1(game.position[1], 1), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        self.assertEqual(game.move2(game.position[2], 2), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        y y y 0 0 0 0
        r r r 0 0 0 0
        """

        # p1 should win
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_horizontal_p2(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[0], 0), True)
        self.assertEqual(game.move1(game.position[1], 1), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        self.assertEqual(game.move2(game.position[2], 2), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[4], 4), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        y y y 0 r 0 0
        r r r y r 0 0
        """

        # p2 should win
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_winning_move_vertical_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        r y 0 0 0 0 0
        r y 0 0 0 0 0
        r y 0 0 0 0 0
        """

        # p1 should win
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_vertical_p2(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[2], 2), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        r y 0 0 0 0 0
        r y 0 0 0 0 0
        r y r 0 0 0 0
        """

        # p2 should win
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_winning_move_positive_slope_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[1], 1), True)
        self.assertEqual(game.move2(game.position[2], 2), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[2], 2), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[3], 3), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 r y 0 0 0
        0 r y r 0 0 0
        r y y r y 0 0
        """

        # p1 should win
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_positive_slope_p2(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[0], 0), True)
        self.assertEqual(game.move2(game.position[1], 1), True)
        self.assertEqual(game.move1(game.position[1], 1), True)
        self.assertEqual(game.move2(game.position[2], 2), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[2], 2), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.move1(game.position[6], 6), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 r y y 0 0
        0 r y r r 0 0
        r y y r y 0 r
        """

        # p2 should win
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_winning_move_negative_slope_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[6], 6), True)
        self.assertEqual(game.move2(game.position[5], 5), True)
        self.assertEqual(game.move1(game.position[5], 5), True)
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[0], 0), True)

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 r r 0 0
        0 0 0 y r r 0
        y 0 0 y y y r
        """

        # p1 should win
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_negative_slope_p2(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'

        # make sure each move is valid
        self.assertEqual(game.move1(game.position[5], 5), True)
        self.assertEqual(game.move2(game.position[6], 6), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[5], 5), True)
        self.assertEqual(game.move1(game.position[4], 4), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[3], 3), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        self.assertEqual(game.move2(game.position[3], 3), True)
        self.assertEqual(game.move1(game.position[2], 2), True)
        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 y 0 0 0
        0 0 0 y 0 0 0
        0 0 r r r y 0
        0 0 r y r r y
        """

        # p2 should win
        self.assertEqual(game.move2(game.position[4], 4), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_winning_move_by_board_positive_slope_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = 'p1'

        """
        game.board = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
        ]
        """

        game.board = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', 'red', '', '', ''],
            ['', '', '', 'yellow', '', '', ''],
            ['', 'red', 'yellow', 'red', '', '', ''],
            ['red', 'yellow', 'yellow', 'red', 'yellow', '', ''],
        ]
        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 r 0 0 0
        0 0 0 y 0 0 0
        0 r y r 0 0 0
        r y y r y 0 0
        """

        # p1 should win
        self.assertEqual(game.move1(3, 2), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_by_board_positive_slope_p2(self):
        game = Gameboard()
        game.player1 = 'yellow'
        game.player2 = 'red'
        game.current_turn = 'p2'
        game.board = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', 'red', '', '', ''],
            ['', '', '', 'yellow', '', '', ''],
            ['', 'red', 'yellow', 'red', '', '', ''],
            ['red', 'yellow', 'yellow', 'red', 'yellow', 'yellow', ''],
        ]

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 r 0 0 0
        0 0 0 y 0 0 0
        0 r y r 0 0 0
        r y y r y y 0
        """

        # p2 should win
        self.assertEqual(game.move2(3, 2), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_winning_move_by_board_negative_slope_p1(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = 'p1'
        game.board = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', 'red', '', '', '', ''],
            ['', '', 'yellow', '', '', '', ''],
            ['', '', 'red', 'red', 'red', 'yellow', ''],
            ['', '', 'yellow', 'yellow', 'yellow', 'red', ''],
        ]

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 r 0 0 0 0
        0 0 y 0 0 0 0
        0 0 r r r y 0
        0 0 y y y r 0
        """

        # p1 should win
        self.assertEqual(game.move1(3, 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p1')

    def test_winning_move_by_board_negative_slope_p2(self):
        game = Gameboard()
        game.player1 = 'yellow'
        game.player2 = 'red'
        game.current_turn = 'p2'
        game.board = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', 'red', '', '', '', ''],
            ['', '', 'yellow', '', '', 'yellow', ''],
            ['', '', 'red', 'red', 'red', 'yellow', ''],
            ['', '', 'yellow', 'yellow', 'yellow', 'red', ''],
        ]

        """
        current board:
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 r 0 0 0 0
        0 0 y 0 0 y 0
        0 0 r r r y 0
        0 0 y y y r 0
        """

        # p2 should win
        self.assertEqual(game.move2(3, 3), True)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.game_result, 'p2')

    def test_invalid_move_out_of_board_positive(self):
        game = Gameboard()
        self.assertEqual(game.move1(1234, 5678), False)
        self.assertEqual(game.out_of_board(1234, 5678), True)

    def test_invalid_move_out_of_board_negative(self):
        game = Gameboard()
        self.assertEqual(game.move1(-1234, -5678), False)
        self.assertEqual(game.out_of_board(-1234, -5678), True)
