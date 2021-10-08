from flask import Flask, render_template, request, jsonify  # , redirect
# from json import dump
from Gameboard import Gameboard
import db
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


game = Gameboard()

'''
Implement '/' endpoint
Method Type: GET
return: template player1_connect.html and status = "Pick a Color."
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def player1_connect():
    global game
    game = Gameboard()
    db.clear()
    db.init_db()
    return render_template('player1_connect.html', status='Pick a Color.')


'''
Helper function that sends to all boards don't modify
'''


@app.route('/autoUpdate', methods=['GET'])
def updateAllBoards():
    try:
        return jsonify(move=game.board, winner=game.game_result,
                       color=game.player1)
    except Exception:
        return jsonify(move="")


'''
Implement '/p1Color' endpoint
Method Type: GET
return: template player1_connect.html and status = <Color picked>
Assign player1 their color
'''


@app.route('/p1Color', methods=['GET'])
def player1_config():
    global game
    data = db.getMove()
    # print("p1 color")
    # print(data)
    if not data:
        game.player1 = request.args.get('color')
        if game.player1 != 'red' and game.player1 != 'yellow':
            exit()
    else:
        game.current_turn = data[0]
        game.board = data[1][0]
        game.position = data[1][1]
        game.game_result = data[2]
        game.player1 = data[3]
        game.player2 = data[4]
        game.remaining_moves = data[5]
    return render_template('player1_connect.html', status=f"{game.player1}")


'''
Implement '/p2Join' endpoint
Method Type: GET
return: template p2Join.html and status = <Color picked> or Error
if P1 didn't pick color first

Assign player2 their color
'''


@app.route('/p2Join', methods=['GET'])
def p2Join():
    global game
    data = db.getMove()
    # print("p2 join")
    # print(data)
    if not data:
        if game.player1 == 'red':
            game.player2 = 'yellow'
        elif game.player1 == 'yellow':
            game.player2 = 'red'
        else:
            return "P1 didn't pick color first", 400
    else:
        game.current_turn = data[0]
        game.board = data[1][0]
        game.position = data[1][1]
        game.game_result = data[2]
        game.player1 = data[3]
        game.player2 = data[4]
        game.remaining_moves = data[5]
    return render_template('p2Join.html', status=f"{game.player2}")


'''
Implement '/move1' endpoint
Method Type: POST
return: jsonify (move=<CurrentBoard>,
invalid=True or False, winner = <currWinner>)
If move is valid --> invalid = False else invalid = True
If invalid == True, also return reason= <Why Move is Invalid>

Process Player 1's move
'''


@app.route('/move1', methods=['POST'])
def p1_move():
    global game
    col = int(request.json['column'][-1]) - 1
    row = game.position[col]
    # print("p1 move")
    # print(game.current_turn)
    # print(game.board)

    # checking all conditions
    if game.player_not_yet_select_color():
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Players need to select color first',
            winner=game.game_result
        )

    if game.game_draw():
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Draw',
            winner=game.game_result
        )

    if game.invalid_turn('p1'):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Not your turn',
            winner=game.game_result
        )

    if game.game_over():
        return jsonify(
            move=game.board,
            invalid=True,
            reason=f'Winner is {game.game_result}',
            winner=game.game_result
        )

    if game.column_full(col):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='You tried to insert into a filled column',
            winner=game.game_result
        )

    if game.out_of_board(row, col):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Out of board',
            winner=game.game_result
        )

    # p1 starts to move
    game.move1(row, col)
    # if game.game_result != '':
    #    db.clear()
    # else:
    db.add_move(game)
    return jsonify(
        move=game.board,
        invalid=False,
        winner=game.game_result
    )


'''
Same as '/move1' but instead proccess Player 2
'''


@app.route('/move2', methods=['POST'])
def p2_move():
    global game
    col = int(request.json['column'][-1]) - 1
    row = game.position[col]
    # print("p2 move")
    # print(game.current_turn)
    # print(game.board)

    # checking all conditions
    if game.player_not_yet_select_color():
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Players need to select color first',
            winner=game.game_result
        )

    if game.game_draw():
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Draw',
            winner=game.game_result
        )

    if game.invalid_turn('p2'):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Not your turn',
            winner=game.game_result
        )

    if game.game_over():
        return jsonify(
            move=game.board,
            invalid=True,
            reason=f'Winner is: {game.game_result}',
            winner=game.game_result
        )

    if game.column_full(col):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='You tried to insert into a filled column',
            winner=game.game_result
        )

    if game.out_of_board(row, col):
        return jsonify(
            move=game.board,
            invalid=True,
            reason='Out of board',
            winner=game.game_result
        )
    # p2 starts to move
    game.move2(row, col)
    # if game.game_result != '':
    #    db.clear()
    # else:
    db.add_move(game)
    return jsonify(
        move=game.board,
        invalid=False,
        winner=game.game_result
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
