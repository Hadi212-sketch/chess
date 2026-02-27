from board import Board

board = Board()

print("=== Move 1: BLACK Pawn a2 forward ===")
board.squares['a2'].move()

print("=== Move 2: WHITE Pawn a7 forward ===")
board.squares['a7'].move()

print("=== Move 3: BLACK Knight b1 forward_left ===")
board.squares['b1'].move('forward_left')

print("\n=== Replaying saved states via generator ===")
states = Board.load_board_states()
for i, state in enumerate(states):
    print(f"\n--- State {i+1} ---")
    Board.print_saved_state(state)
