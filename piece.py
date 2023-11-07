class Piece:

    def __init__(self, color: str, row: int, col: int,board):
        self.color = color
        self.col = col
        self.row = row  
        self.name = None
        self.board = board


    def set_image(self, image):
        self.image = image


    def get_image(self):
        return self.image
        

    def get_color(self):
        return self.color
    

    def move_possibility(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8


    def get_piece_coordinates(self):
        return self.row, self.col
    

    def get_image_path(self):
        raise NotImplementedError("Subclasses must implement get_image_path")


    def get_type(self):
        return self.__class__.__name__
        

    def move(self, new_row, new_col):
        if self.is_valid_move(self, new_row, new_col):
            self.board.remove_piece(self)  
            self.set_position(new_row, new_col)  
            self.board.add_piece(self, new_row, new_col)  
            return True
        else:
            return False
    

    def remove_piece(self,piece):
        self.board.remove_piece(self,piece)
    

    def add_piece(self, new_row, new_col):
        self.board.add_piece(self, new_row, new_col)
    

    def set_position(self, new_row, new_col):
        self.row = new_row
        self.col = new_col


    def is_valid_move(self, piece_to_move, new_row, new_col):
        current_row, current_col = self.get_piece_coordinates()
        piece_color = self.get_color()

        possible_moves = self.movement()

        if (new_row, new_col) in possible_moves:
            for piece, (row, col) in self.board.pieces.items():
                if row == new_row and col == new_col and piece.get_color() == piece_color:
                    return False
            return True

        return False


class Pawn(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = []
        if self.color == "white":
            if self.row > 0:
                moves.append((self.row - 1, self.col))
                if self.row == 6:
                    moves.append((self.row - 2, self.col))
            if self.row > 0 and self.col > 0:
                moves.append((self.row - 1, self.col - 1))
            if self.row > 0 and self.col < 7:
                moves.append((self.row - 1, self.col + 1))
        else:
            if self.row < 7:
                moves.append((self.row + 1, self.col))
                if self.row == 1:
                    moves.append((self.row + 2, self.col))
            if self.row < 7 and self.col > 0:
                moves.append((self.row + 1, self.col - 1))
            if self.row < 7 and self.col < 7:
                moves.append((self.row + 1, self.col + 1))

        return moves


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whitePawn.png"
        else:
            return "images/blackPawn.png"       


class Knight(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = [
            (self.row - 2, self.col + 1), (self.row - 1, self.col + 2),
            (self.row + 1, self.col + 2), (self.row + 2, self.col + 1),
            (self.row + 2, self.col - 1), (self.row + 1, self.col - 2),
            (self.row - 1, self.col - 2), (self.row - 2, self.col - 1)
        ]

        return [(row, col) for row, col in moves if self.move_possibility(row, col)]


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteKnight.png"
        else:
            return "images/blackKnight.png"
        

class Bishop(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = set()
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:
            row, col = self.row, self.col
            for _ in range(1, 8):
                row += direction[0]
                col += direction[1]
                if self.move_possibility(row, col):
                    moves.add((row, col))
                else:
                    break
        return list(moves)


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteBishop.png"
        else:
            return "images/blackBishop.png"
        

    def is_valid_move(self, piece_to_move, new_row, new_col):
        current_row, current_col = self.get_piece_coordinates()
        piece_color = self.get_color()

        bishop_moves = self.movement()

        if (new_row, new_col) in bishop_moves:
            row_step = 1 if new_row > current_row else -1
            col_step = 1 if new_col > current_col else -1
            col, row = current_col + col_step, current_row + row_step
            while col != new_col or row != new_row:
                if self.board.get_piece_at(row, col):
                    if self.board.get_piece_at(row, col).get_color() == piece_color:
                        return False
                col += col_step
                row += row_step
            return True

        return False


class Rook(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = []
        for col in range(8):
            if col != self.col:
                moves.append((self.row, col))

        for row in range(8):
            if row != self.row:
                moves.append((row, self.col))
        return moves


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteRook.png"
        else:
            return "images/blackRook.png"


class Queen(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = set()

        for col in range(8):
            if col != self.col:
                moves.add((self.row, col))

        for row in range(8):
            if row != self.row:
                moves.add((row, self.col))

        for dr in [-1, 1]:
            for dc in [-1, 1]:
                row, col = self.row + dr, self.col + dc
                while self.move_possibility(row, col):
                    moves.add((row, col))
                    row += dr
                    col += dc

        return list(moves)


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteQueen.png"
        else:
            return "images/blackQueen.png"
        

class King(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)


    def movement(self):
        moves = [
            (self.row - 1, self.col), (self.row - 1, self.col + 1),
            (self.row, self.col + 1), (self.row + 1, self.col + 1),
            (self.row + 1, self.col), (self.row + 1, self.col - 1),
            (self.row, self.col - 1), (self.row - 1, self.col - 1)
        ]
        return [move for move in moves if self.move_possibility(*move)]


    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whiteKing.png"
        else:
            return "images/blackKing.png"
        

    def is_valid_move(self, piece_to_move, new_row, new_col):
        current_row, current_col = self.get_piece_coordinates()
        piece_color = self.get_color()

        for piece, (col, row) in self.board.pieces.items():
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False
            moves = [
                (current_row - 1, current_col), (current_row - 1, current_col + 1),
                (current_row, current_col + 1), (current_row + 1, current_col + 1),
                (current_row + 1, current_col), (current_row + 1, current_col - 1),
                (current_row, current_col - 1), (current_row - 1, current_col - 1)
            ]
            if (new_row, new_col) in moves:
                return True
            return False
        
        return True


class EmptyCell(Piece):

    def __init__(self, row=None, col=None, board=None):
        super().__init__(None, None, None, None)
        self.value = "empty" 


    def get_value(self):
        return self.value


    def set_value(self, new_value):
        self.value = new_value


    def get_image_path(self):
        return None
    