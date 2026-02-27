from abc import ABC, abstractmethod


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
        print(movement)

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

    def move(self, movement=None):
        movement = "Pawn moves forward 1 position"
        super().move(movement)


class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Rook', 'R', identifier)

    def move(self, movement=None):
        movement = "Rook moves in a straight line"
        super().move(movement)


class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Bishop', 'B', identifier)

    def move(self, movement=None):
        movement = "Bishop moves diagonally"
        super().move(movement)


class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Knight', 'N', identifier)

    def move(self, movement=None):
        movement = "Knight moves in an L shape"
        super().move(movement)


class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'King', 'K', identifier)

    def move(self, movement=None):
        movement = "King moves one position in any direction"
        super().move(movement)


class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, 'Queen', 'Q', identifier)

    def move(self, movement=None):
        movement = "Queen moves in any direction"
        super().move(movement)
