import sqlite3
from sqlite3 import Error
import json
'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)
        return "init error"

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move):  # will take in a tuple
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO GAME(
            current_turn,
            board,
            winner,
            player1,
            player2,
            remaining_moves
            ) VALUES(?, ?, ?, ?, ?, ?);""",
            (
                move.current_turn,
                json.dumps([move.board, move.position]),
                move.game_result,
                move.player1,
                move.player2,
                move.remaining_moves
            )
        )
        conn.commit()
    except Error as e:
        print(e)
        return "add_move error"

    finally:
        if conn:
            conn.close()


'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM GAME ORDER BY remaining_moves
            ASC LIMIT 1;""")

        data = cursor.fetchone()
        if not data:
            return data
        data = list(data)
        data[1] = json.loads(data[1])
        return data
    except Error as e:
        print(e)
        return "get_move error"

    finally:
        if conn:
            conn.close()


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
