class BoardMovement:

    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])
        new_row = row + squares if color == 'BLACK' else row - squares
        if new_row < 1 or new_row > 8:
            print(f"Movement blocked: out of bounds")
            return position
        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])
        new_row = row - squares if color == 'BLACK' else row + squares
        if new_row < 1 or new_row > 8:
            print(f"Movement blocked: out of bounds")
            return position
        return f"{column}{new_row}"

    @staticmethod
    def left(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) - squares) if color == 'BLACK' else chr(ord(column) + squares)
        if new_column == '' or new_column == 'i':
            print(f"Movement blocked: out of bounds")
            return position
        return f"{new_column}{row}"

    @staticmethod
    def right(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) + squares) if color == 'BLACK' else chr(ord(column) - squares)
        if new_column == '' or new_column == 'i':
            print(f"Movement blocked: out of bounds")
            return position
        return f"{new_column}{row}"

    @staticmethod
    def forward_left(position: str, color: str, squares: int = 1):
        new_pos = BoardMovement.forward(position, color, squares)
        return BoardMovement.left(new_pos, color, squares)

    @staticmethod
    def forward_right(position: str, color: str, squares: int = 1):
        new_pos = BoardMovement.forward(position, color, squares)
        return BoardMovement.right(new_pos, color, squares)

    @staticmethod
    def backward_left(position: str, color: str, squares: int = 1):
        new_pos = BoardMovement.backward(position, color, squares)
        return BoardMovement.left(new_pos, color, squares)

    @staticmethod
    def backward_right(position: str, color: str, squares: int = 1):
        new_pos = BoardMovement.backward(position, color, squares)
        return BoardMovement.right(new_pos, color, squares)
