import chess

board = chess.Board()

counter = 0

while not board.is_game_over():
    if counter % 2 == 0:
        player = "White"
    else:
        player = "Black"

    move_str = input(f"Enter a move for {player}: ")
    try:
        move = chess.Move.from_uci(move_str)
    except ValueError:
        print("Invalid move format. Please try again.")
        continue

    if move not in board.legal_moves:
        print("Illegal move. Please try again.")
        continue

    board.push(move)
    counter += 1

    print(board)

winner = "White" if not board.turn else "Black"
print(f"{winner} wins!")