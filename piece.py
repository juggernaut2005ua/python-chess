class Piece:

    def __init__(self, color: str, row: int, col: int,board):
        self.color = color
        self.col = col
        self.row = row  
        self.name = None
        self.isPicked = False
        self.board = board

        

    def get_color(self):
        return self.color
    
    def is_piece_picked(self):
        return self.isPicked

    # def is_valid_move(self, new_col, new_row, board):
    #     if self.move_possibility(new_col, new_row):
    #         piece_at_new_position = board.get_piece_at(new_row, new_col)
    #         return piece_at_new_position is None or piece_at_new_position.get_color() != self.get_color()
    #     return False

    def move_possibility(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece_coordinates(self):
        return self.row, self.col
    
    def get_image_path(self):
        raise NotImplementedError("Subclasses must implement get_image_path")

    def get_type(self):
        return self.__class__.__name__
    
        
    # def move_piece(self, piece_to_move, new_row, new_col):
    #     # Проверяем, допустим ли такой ход
    #     if self.is_valid_move(self, new_row, new_col):
    #         # Выполняем перемещение фигуры
    #         self.move(self, new_row, new_col)
    #         return True
    #     else:
    #         return False
        
    def move(self, new_row, new_col):
        if self.is_valid_move(self, new_row, new_col):
            self.board.remove_piece(self)  # Удалить фигуру с текущей позиции
            self.set_position(new_row, new_col)  # Установить новые координаты
            self.board.add_piece(self, new_row, new_col)  # Добавить фигуру на новую позицию
            return True
        else:
            return False
    
    def remove_piece(self):
        self.board.remove_piece(self)
    
    def add_piece(self, new_row, new_col):
        self.board.add_piece(self, new_row, new_col)
    
    def set_position(self, new_row, new_col):
        # Установите новые координаты фигуры
        self.row = new_row
        self.col = new_col


class Pawn(Piece):

    def __init__(self, color: str, row: int, col: int, board):
        super().__init__(color, row, col, board)

    def movement(self):
        moves = []
        if self.color == "white":
            moves.append((self.row - 1, self.col))
            if self.row == 6:
                moves.append((self.row - 2, self.col))
            moves.append((self.row - 1, self.col - 1))
            moves.append((self.row - 1, self.col + 1))
        else:
            moves.append((self.row + 1, self.col))
            if self.row == 1:
                moves.append((self.row + 2, self.col))
            moves.append((self.row + 1, self.col - 1))
            moves.append((self.row + 1, self.col + 1))
        return moves

    def get_image_path(self):
        if self.get_color() == "white":
            return "images/whitePawn.png"
        else:
            return "images/blackPawn.png"
        
    def is_valid_move(self, piece_to_move, new_row, new_col):   
        current_row, current_col = self.get_piece_coordinates()
        piece_color = self.get_color()

        # Проверяем, что целевой квадрат не занят фигурой того же цвета.
        for piece, (row, col) in self.board.pieces.items():
            if row == new_row and col == new_col and piece.get_color() == piece_color:
                return False

        # Проверяем правила для пешки (движение вперед и захват по диагонали).
        if piece_color == "white":
            if current_row == 1:
                # Пешка в начальной позиции может двигаться на две клетки вперед.
                if (new_row, new_col) == (current_row + 2, current_col) and (new_row - 1, new_col) not in self.board.pieces.values():
                    return True
            if (new_row, new_col) == (current_row + 1, current_col) and (new_row, new_col) not in self.board.pieces.values():
                return True
            if (new_row, new_col) in self.board.pieces.values() and (new_row, new_col) != (current_row + 1, current_col):
                return True
        else:
            if current_row == 6:
                # Пешка в начальной позиции может двигаться на две клетки вперед.
                if (new_row, new_col) == (current_row - 2, current_col) and (new_row + 1, new_col) not in self.board.pieces.values():
                    return True
            if (new_row, new_col) == (current_row - 1, current_col) and (new_row, new_col) not in self.board.pieces.values():
                return True
            if (new_row, new_col) in self.board.pieces.values() and (new_row, new_col) != (current_row - 1, current_col):
                return True

        return False




    # def move(self, board_logic, new_row, new_col):
    #     # Ваша логика проверки допустимости хода
    #     if self.is_valid_move(board_logic, new_row, new_col):
    #         # Переместить фигуру на новую позицию
    #         self.remove_piece(self)
    #         self.set_position(new_row, new_col)
    #         self.add_piece(self,new_row,new_col)
    #         return True
    #     else:
    #         return False
        
    # def move_piece(self, piece_to_move, new_col, new_row):
    #     # Проверяем, допустим ли такой ход
    #     if piece_to_move.is_valid_move(self, new_col, new_row):
    #         # Выполняем перемещение фигуры
    #         piece_to_move.move(self, new_col, new_row)
    #         return True
    #     else:
    #         return False
        
    



class Knight(Piece):

    def __init__(self, color: str, col: int, row: int, board):
        super().__init__(color, col, row, board)

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
        
    def is_valid_move(self, board_logic, new_col, new_row):
        current_col, current_row = self.get_piece_coordinates()
        piece_color = self.get_color()

        for piece, (col, row) in self.board.pieces.items():
            # Перевірте, чи цільовий квадрат зайнятий іншою фігурою того ж кольору.
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False

        moves = [
            (current_col + 1, current_row - 2), (current_col + 2, current_row - 1),
            (current_col + 2, current_row + 1), (current_col + 1, current_row + 2),
            (current_col - 1, current_row + 2), (current_col - 2, current_row + 1),
            (current_col - 2, current_row - 1), (current_col - 1, current_row - 2)
        ]

        # Перевірка, чи нова позиція знаходиться серед можливих ходів коня
        if (new_col, new_row) in moves:
            return True

        return False



class Bishop(Piece):

    def __init__(self, color: str, col: int, row: int, board):
        super().__init__(color, col, row, board)

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
        
    def is_valid_move(self, piece_to_move, new_col, new_row):
        current_col, current_row = self.get_piece_coordinates()
        piece_color = self.get_color()

        if abs(current_col - new_col) == abs(current_row - new_row):
            col_step = 1 if new_col > current_col else -1
            row_step = 1 if new_row > current_row else -1
            col, row = current_col + col_step, current_row + row_step
            while col != new_col:
                if self.board.get_piece_at(row, col):
                    return False
                col += col_step
                row += row_step
            return True  # Повернути True, якщо це можливий хід для слона
        else:
            return False



class Rook(Piece):

    def __init__(self, color: str, col: int, row: int, board):
        super().__init__(color, col, row, board)

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
        
    def is_valid_move(self, piece_to_move, new_col, new_row):
        current_col, current_row = self.get_piece_coordinates()
        piece_color = self.get_color()

        for piece, (col, row) in self.board.pieces.items():
            # Перевірте, чи цільовий квадрат зайнятий іншою фігурою того ж кольору.
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False
            if current_col == new_col or current_row == new_row:
                # Проверка наличия фигур на пути
                if current_col == new_col:
                    min_row, max_row = min(current_row, new_row), max(current_row, new_row)
                    for row in range(min_row + 1, max_row):
                        if self.board.get_piece_at(row, current_col):
                            return False
                else:
                    min_col, max_col = min(current_col, new_col), max(current_col, new_col)
                    for col in range(min_col + 1, max_col):
                        if self.board.get_piece_at(current_row, col):
                            return False
                        
        return True 


class Queen(Piece):

    def __init__(self, color: str, col: int, row: int, board):
        super().__init__(color, col, row, board)

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
        
    def is_valid_move(self, piece_to_move, new_col, new_row):
        current_col, current_row = self.get_piece_coordinates()
        piece_color = self.get_color()

        for piece, (col, row) in self.board.pieces.items():
            # Перевірте, чи цільовий квадрат зайнятий іншою фігурою того ж кольору.
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False
            # Проверка вертикальных и горизонтальных ходов, аналогично ладье
            if current_col == new_col or current_row == new_row:
                # Проверка наличия фигур на пути
                if current_col == new_col:
                    min_row, max_row = min(current_row, new_row), max(current_row, new_row)
                    for row in range(min_row + 1, max_row):
                        if self.board.get_piece_at(row, current_col):
                            return False
                else:
                    min_col, max_col = min(current_col, new_col), max(current_col, new_col)
                    for col in range(min_col + 1, max_col):
                        if self.board.get_piece_at(current_row, col):
                            return False
            # Проверка диагональных ходов, аналогично слону
            elif abs(current_col - new_col) == abs(current_row - new_row):
                col_step = 1 if new_col > current_col else -1
                row_step = 1 if new_row > current_row else -1
                col, row = current_col + col_step, current_row + row_step
                while col != new_col:
                    if self.board.get_piece_at(row, col):
                        return False
                    col += col_step
                    row += row_step
            else:
                return False
        return True


class King(Piece):

    def __init__(self, color: str, col: int, row: int, board):
        super().__init__(color, col, row, board)

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
        
    def is_valid_move(self, piece_to_move, new_col, new_row):
        current_col, current_row = self.get_piece_coordinates()
        piece_color = self.get_color()

        for piece, (col, row) in self.board.pieces.items():
            # Перевірте, чи цільовий квадрат зайнятий іншою фігурою того ж кольору.
            if col == new_col and row == new_row and piece.get_color() == piece_color:
                return False
            moves = [
                (current_col, current_row - 1), (current_col + 1, current_row - 1),
                (current_col + 1, current_row), (current_col + 1, current_row + 1),
                (current_col, current_row + 1), (current_col - 1, current_row + 1),
                (current_col - 1, current_row), (current_col - 1, current_row - 1)
            ]
            if (new_col, new_row) in moves:
                return True
            return False
        
        return True

class EmptyCell(Piece):
    def __init__(self, row, col, board):
        super().__init__(None, row, col, board)
        self.value = "empty"  # None означает, что у пустой клетки нет цвета

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_image_path(self):
        return None