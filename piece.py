class Piece:

    def __init__(self, color: str, col: int, row: int):
        self.color = color
        self.col = col
        self.row = row  
        self.name = None
        self.isPicked = False

    def get_color(self):
        return self.color
    
    def is_piece_picked(self):
        return self.isPicked

    def is_valid_move(self, new_col, new_row, board):
        if self.move_possibility(new_col, new_row):
            piece_at_new_position = board.get_piece_at(new_row, new_col)
            return piece_at_new_position is None or piece_at_new_position.get_color() != self.get_color()
        return False

    def move_possibility(self, col, row):
        return 0 <= col < 8 and 0 <= row < 8

    def get_piece_coordinates(self):
        return self.col, self.row
    
    def get_image_path(self):
        raise NotImplementedError("Subclasses must implement get_image_path")

    def get_type(self):
        return self.__class__.__name__


class Pawn(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = []
        if self.color == "white":
            moves.append((self.col, self.row - 1))
            if self.row == 6:
                moves.append((self.col, self.row - 2))
            moves.append((self.col - 1, self.row - 1))
            moves.append((self.col + 1, self.row - 1))
        else:
            moves.append((self.col, self.row + 1))
            if self.row == 1:
                moves.append((self.col, self.row + 2))
            moves.append((self.col - 1, self.row + 1))
            moves.append((self.col + 1, self.row + 1))
        return moves

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whitePawn.png"
        else:
            return "images/blackPawn.png"
        
    def is_valid_move(self, piece_to_move, new_col, new_row):
        current_col, current_row = piece_to_move.get_piece_coordinates()
        piece_color = piece_to_move.get_color()

        for piece, (col, row) in self.pieces.items():
            # Перевірте, чи цільовий квадрат зайнятий іншою фігурою того ж кольору.
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False

            # Перевірка правил для пішака (один або два квадрати вперед і захоплення по діагоналі).
            if piece.get_type() == "Pawn":
                if piece_color == "white":
                    if (col == new_col and row == current_row + 1) or (col == new_col and row == current_row - 1):
                        return False
                    if current_row == 1 and (new_col, new_row) == (current_col, current_row + 2):
                        return False
                else:
                    if (col == new_col and row == current_row - 1) or (col == new_col and row == current_row + 1):
                        return False
                    if current_row == 6 and (new_col, new_row) == (current_col, current_row - 2):
                        return False

        # Якщо жодна з умов вище не виконується, хід вважається допустимим.
        return True

    def move_piece(self, piece_to_move, new_col, new_row):
        # Проверяем, допустим ли такой ход
        if piece_to_move.is_valid_move(self, new_col, new_row):
            # Выполняем перемещение фигуры
            piece_to_move.move(self, new_col, new_row)
            return True
        else:
            return False



class Knight(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = [
            (self.col + 1, self.row - 2), (self.col + 2, self.row - 1),
            (self.col + 2, self.row + 1), (self.col + 1, self.row + 2),
            (self.col - 1, self.row + 2), (self.col - 2, self.row + 1),
            (self.col - 2, self.row - 1), (self.col - 1, self.row - 2)
        ]
        return [move for move in moves if self.move_possibility(*move)]

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteKnight.png"
        else:
            return "images/blackKnight.png"


class Bishop(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = set() 
        for i in range(1, 8):
            col, row = self.col - i, self.row - i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col - i, self.row + i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col + i, self.row + i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col + i, self.row - i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        return list(moves)

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteBishop.png"
        else:
            return "images/blackBishop.png"


class Rook(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = []
        for col in range(8):
            if col != self.col:
                moves.append((col, self.row))

        for row in range(8):
            if row != self.row:
                moves.append((self.col, row))
        return moves

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteRook.png"
        else:
            return "images/blackRook.png"


class Queen(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = set()

        for col in range(8):
            if col != self.col:
                moves.add((col, self.row))

        for row in range(8):
            if row != self.row:
                moves.add((self.col, row))

        for i in range(1, 8):
            col, row = self.col - i, self.row - i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col - i, self.row + i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col + i, self.row + i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        for i in range(1, 8):
            col, row = self.col + i, self.row - i
            if self.move_possibility(col, row):
                moves.add((col, row))
            else:
                break

        return list(moves)

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteQueen.png"
        else:
            return "images/blackQueen.png"


class King(Piece):

    def __init__(self, color: str, col: int, row: int):
        super().__init__(color, col, row)

    def movement(self):
        moves = [
            (self.col, self.row - 1), (self.col + 1, self.row - 1),
            (self.col + 1, self.row), (self.col + 1, self.row + 1),
            (self.col, self.row + 1), (self.col - 1, self.row + 1),
            (self.col - 1, self.row), (self.col - 1, self.row - 1)
        ]
        return [move for move in moves if self.move_possibility(*move)]

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteKing.png"
        else:
            return "images/blackKing.png"


test = Piece("white",1,1)
print(test.get_color())