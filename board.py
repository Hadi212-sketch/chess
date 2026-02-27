import json
from pieces import Rook, Knight, Bishop, Queen, King, Pawn


class Board:
    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }
        self.setup_board()

        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def setup_board(self):
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)

        black_pawns = {f"{chr(col)}2": Pawn('BLACK', col - ord('a') + 1) for col in range(ord('a'), ord('i'))}
        self.squares.update(black_pawns)

        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)

        white_pawns = {f"{chr(col)}7": Pawn('WHITE', col - ord('a') + 1) for col in range(ord('a'), ord('i'))}
        self.squares.update(white_pawns)

    def print_board(self):
        rows = [
            [self.squares[f"{chr(col)}{row}"] for col in range(ord('a'), ord('i'))]
            for row in range(1, 9)
        ]
        for row in rows:
            print(row)

    def save_board(self):
        with open('board.txt', 'a') as file:
            file.write(json.dumps(self.squares) + '\n')

    @staticmethod
    def load_board_states():
        with open('board.txt', 'r') as file:
            for line in file:
                yield json.loads(line)

    @staticmethod
    def print_saved_state(state: dict):
        rows = [
            [state.get(f"{chr(col)}{row}") for col in range(ord('a'), ord('i'))]
            for row in range(1, 9)
        ]
        for row in rows:
            print(row)

    def find_piece(self, symbol: str, identifier: int, color: str):
        return [piece for square, piece in self.squares.items()
                if piece is not None
                and piece.symbol == symbol
                and piece.identifier == identifier
                and piece.color == color]

    def get_piece(self, square):
        return self.squares[square]

    def is_square_empty(self, square):
        return self.get_piece(square) is None

    def kill_piece(self, square):
        piece = self.squares[square]
        if piece is not None:
            piece.die()
            self.squares[square] = None
