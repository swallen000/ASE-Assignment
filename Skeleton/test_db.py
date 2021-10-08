import unittest
from Gameboard import Gameboard
import db


class Test_DB(unittest.TestCase):

    def test_empty_db(self):
        db.clear()
        db.init_db()
        data = db.getMove()
        self.assertEqual(None, data)
        db.clear()

    def test_init_error(self):
        db.clear()
        db.init_db()
        data = db.init_db()
        self.assertEqual("init error", data)
        db.clear()

    def test_add_move_error(self):
        db.clear()
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = 'p1'
        game.remaining_moves = 42
        data = db.add_move(game)
        self.assertEqual("add_move error", data)

    def test_get_move_error(self):
        db.clear()
        data = db.getMove()
        self.assertEqual("get_move error", data)

    def test_add_move(self):
        db.clear()
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = 'p1'
        game.remaining_moves = 42
        db.init_db()
        db.add_move(game)
        data = db.getMove()
        # print(data)
        self.assertEqual(game.player1, data[3])
        self.assertEqual(game.player2, data[4])
        self.assertEqual(game.current_turn, data[0])
        self.assertEqual(game.board, data[1][0])
        self.assertEqual(game.position, data[1][1])
        self.assertEqual(game.remaining_moves, data[5])
        self.assertEqual(game.game_result, data[2])

        game.current_turn = 'p2'
        game.remaining_moves = 41
        db.add_move(game)
        data = db.getMove()
        self.assertEqual(game.player1, data[3])
        self.assertEqual(game.player2, data[4])
        self.assertEqual(game.current_turn, data[0])
        self.assertEqual(game.board, data[1][0])
        self.assertEqual(game.position, data[1][1])
        self.assertEqual(game.remaining_moves, data[5])
        self.assertEqual(game.game_result, data[2])
        db.clear()


"""
if __name__ == '__main__':
    unittest.main()
"""
