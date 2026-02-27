from abc import ABC, abstractmethod
import functools


def print_board(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board is not None:
            self.board.print_board()
            self.board.save_board()
        return result
    return wrapper


class BaseChessPiece(ABC, dict):
    def __init__(self, color, name, symbol, identifier):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = 'None'
        self.is_alive = True
        self.board = None
        dict.__init__(self, color=color, name=name, symbol=symbol, identifier=identifier)

    @abstractmethod
    def move(self, movement):
        if self.board is not None:
            new_location = self.board.get_piece(movement)
            if new_location is not None:
                if new_location.color != self.color:
                    self.board.kill_piece(movement)
                else:
                    print(f"Blocked: {movement} occupied by friendly piece")
                    return
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self
        print(f"{self} moves to {movement}")

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"


class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Pawn', '-', identifier)

    @print_board
    def move(self, movement=None):
        from movements import BoardMovement
        movement = BoardMovement.forward(self.position, self.color, 1)
        super().move(movement)


class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Rook', 'R', identifier)

    @print_board
    def move(self, direction='forward', squares=1):
        from movements import BoardMovement
        directions = {
            'forward': BoardMovement.forward,
            'backward': BoardMovement.backward,
            'left': BoardMovement.left,
            'right': BoardMovement.right
        }
        movement = directions[direction](self.position, self.color, squares)
        super().move(movement)


class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Bishop', 'B', identifier)

    @print_board
    def move(self, direction='forward_right', squares=1):
        from movements import BoardMovement
        directions = {
            'forward_right': BoardMovement.forward_right,
            'forward_left': BoardMovement.forward_left,
            'backward_right': BoardMovement.backward_right,
            'backward_left': BoardMovement.backward_left
        }
        movement = directions[direction](self.position, self.color, squares)
        super().move(movement)


class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Knight', 'N', identifier)

    @print_board
    def move(self, direction='forward_left'):
        from movements import BoardMovement
        knight_moves = {
            'forward_left':  lambda p, c: BoardMovement.left(BoardMovement.forward(p, c, 2), c, 1),
            'forward_right': lambda p, c: BoardMovement.right(BoardMovement.forward(p, c, 2), c, 1),
            'backward_left': lambda p, c: BoardMovement.left(BoardMovement.backward(p, c, 2), c, 1),
            'backward_right':lambda p, c: BoardMovement.right(BoardMovement.backward(p, c, 2), c, 1),
            'left_forward':  lambda p, c: BoardMovement.forward(BoardMovement.left(p, c, 2), c, 1),
            'left_backward': lambda p, c: BoardMovement.backward(BoardMovement.left(p, c, 2), c, 1),
            'right_forward': lambda p, c: BoardMovement.forward(BoardMovement.right(p, c, 2), c, 1),
            'right_backward':lambda p, c: BoardMovement.backward(BoardMovement.right(p, c, 2), c, 1),
        }
        movement = knight_moves[direction](self.position, self.color)
        super().move(movement)


class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'King', 'K', identifier)

    @print_board
    def move(self, direction='forward'):
        from movements import BoardMovement
        directions = {
            'forward': BoardMovement.forward,
            'backward': BoardMovement.backward,
            'left': BoardMovement.left,
            'right': BoardMovement.right,
            'forward_right': BoardMovement.forward_right,
            'forward_left': BoardMovement.forward_left,
            'backward_right': BoardMovement.backward_right,
            'backward_left': BoardMovement.backward_left
        }
        movement = directions[direction](self.position, self.color, 1)
        super().move(movement)


class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Queen', 'Q', identifier)

    @print_board
    def move(self, direction='forward', squares=1):
        from movements import BoardMovement
        directions = {
            'forward': BoardMovement.forward,
            'backward': BoardMovement.backward,
            'left': BoardMovement.left,
            'right': BoardMovement.right,
            'forward_right': BoardMovement.forward_right,
            'forward_left': BoardMovement.forward_left,
            'backward_right': BoardMovement.backward_right,
            'backward_left': BoardMovement.backward_left
        }
        movement = directions[direction](self.position, self.color, squares)
        super().move(movement)
