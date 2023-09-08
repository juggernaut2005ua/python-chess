from piece import Pawn, King, Knight, Bishop, Rook, Queen, Piece
from board import ChessBoardGUI

class GameLogic:
    def __init__(self, board_gui):
        self.pieces = {}
        self.board = [[None for _ in range(8)] for _ in range(8)] # двухмерный массив
        self.board_gui = board_gui
        self.current_player = "white"


    # def initialize_board(self):
    #     # Расставляем начальные фигуры на доске
    #     for i in range(8):
    #         self.add_piece(Pawn("black", 1, i), 1, i)
    #         self.add_piece(Pawn("white",6,i),6, i)
    #     #Rook
    #     self.add_piece(Rook("black", 0, 0), 0, 0)
    #     self.add_piece(Rook("black", 0, 7), 0, 7)
    #     self.add_piece(Rook("white", 7, 0), 7, 0)
    #     self.add_piece(Rook("white", 7, 7), 7, 7)
    #     #Bishop
    #     self.add_piece(Bishop("black",0,2),0,2)
    #     self.add_piece(Bishop("black",0,5),0,5)
    #     self.add_piece(Bishop("white",7,2),7,2)
    #     self.add_piece(Bishop("white",7,5),7,5)
    #     #Knight
    #     self.add_piece(Knight("black",0,1),0,1)
    #     self.add_piece(Knight("black",0,6),0,6)
    #     self.add_piece(Knight("white",7,1),7,1)
    #     self.add_piece(Knight("white",7,6),7,6)
    #     #King
    #     self.add_piece(King("white",7,4),7,4)
    #     self.add_piece(King("black",0,4),0,4)
    #     # Queens
    #     self.add_piece(Queen("white",7,3),7,3)
    #     self.add_piece(Queen("black",0,3),0,3)


        # for piece, position in self.pieces.items():
        #     print(piece, position)

    # def get_piece_at(self, row, col):
    #     return self.board[row][col]
    
    # def add_piece(self, piece, row, col):
    #     self.pieces[piece] = (row, col)
    #     self.board[row][col] = piece

    # def is_valid_move(self, piece_to_move, new_col, new_row):
    #     for piece, (col, row) in self.pieces.items():
    #         if col == new_col and row == new_row:
    #             return False
        
    #     piece_type = piece_to_move.get_type()
    #     current_row, current_col = piece_to_move.get_piece_coordinates()
    #     piece_color = piece_to_move.get_color()

    #     if piece_type == "Queen":
    #         # Проверка вертикальных и горизонтальных ходов, аналогично ладье
    #         if current_col == new_col or current_row == new_row:
    #             # Проверка наличия фигур на пути
    #             if current_col == new_col:
    #                 min_row, max_row = min(current_row, new_row), max(current_row, new_row)
    #                 for row in range(min_row + 1, max_row):
    #                     if self.get_piece_at(row, current_col):
    #                         return False
    #             else:
    #                 min_col, max_col = min(current_col, new_col), max(current_col, new_col)
    #                 for col in range(min_col + 1, max_col):
    #                     if self.get_piece_at(current_row, col):
    #                         return False
    #         # Проверка диагональных ходов, аналогично слону
    #         elif abs(current_col - new_col) == abs(current_row - new_row):
    #             col_step = 1 if new_col > current_col else -1
    #             row_step = 1 if new_row > current_row else -1
    #             col, row = current_col + col_step, current_row + row_step
    #             while col != new_col:
    #                 if self.get_piece_at(row, col):
    #                     return False
    #                 col += col_step
    #                 row += row_step
    #         else:
    #             return False
    #     elif piece_type == "Rook":
    #         if current_col == new_col or current_row == new_row:
    #             # Проверка наличия фигур на пути
    #             if current_col == new_col:
    #                 min_row, max_row = min(current_row, new_row), max(current_row, new_row)
    #                 for row in range(min_row + 1, max_row):
    #                     if self.get_piece_at(row, current_col):
    #                         return False
    #             else:
    #                 min_col, max_col = min(current_col, new_col), max(current_col, new_col)
    #                 for col in range(min_col + 1, max_col):
    #                     if self.get_piece_at(current_row, col):
    #                         return False
    #     elif piece_type == "Bishop":
    #         if abs(current_col - new_col) == abs(current_row - new_row):
    #             col_step = 1 if new_col > current_col else -1
    #             row_step = 1 if new_row > current_row else -1
    #             col, row = current_col + col_step, current_row + row_step
    #             while col != new_col:
    #                 if self.get_piece_at(row, col):
    #                     return False
    #                 col += col_step
    #                 row += row_step
    #         else:
    #             return False
            
    #     elif piece_type == "Pawn":
    #         if piece_color == "white":
    #             for other_piece, (col, row) in self.pieces.items():
    #                 if col == new_col and row == current_row + 1:
    #                     return False
    #         for other_piece, (col, row) in self.pieces.items():
    #             if col == new_col and row == current_row - 1:
    #                 return False
                
    #     elif piece_type == "Knight":
    #         moves = [
    #         (current_col + 1, current_row - 2), (current_col + 2, current_row - 1),
    #         (current_col + 2, current_row + 1), (current_col + 1, current_row + 2),
    #         (current_col - 1, current_row + 2), (current_col - 2, current_row + 1),
    #         (current_col - 2, current_row - 1), (current_col - 1, current_row - 2)
    #         ]
    #     # Проверяем, является ли новая позиция одной из возможных позиций коня
    #         if (new_col, new_row) in moves:
    #             return True
    #     elif piece_type == "King":
    #         # Проверка возможных ходов короля
    #         moves = [
    #             (current_col, current_row - 1), (current_col + 1, current_row - 1),
    #             (current_col + 1, current_row), (current_col + 1, current_row + 1),
    #             (current_col, current_row + 1), (current_col - 1, current_row + 1),
    #             (current_col - 1, current_row), (current_col - 1, current_row - 1)
    #         ]
    #         if (new_col, new_row) in moves:
    #             return True
    #         return False
        
    #     return True
    
    # def move(self, board_logic, new_col, new_row):
    #     # Ваша логика проверки допустимости хода
    #     if self.is_valid_move(board_logic, new_col, new_row):
    #         # Переместить фигуру на новую позицию
    #         self.set_position(new_col, new_row)
    #         return True
    #     else:
    #         return False
        
    # def set_position(self, new_col, new_row):
    #     # Установите новые координаты фигуры
    #     self.col = new_col
    #     self.row = new_row

    
    # def move_piece(self, piece_to_move, new_col, new_row):
    #     # Проверяем, допустим ли такой ход
    #     if piece_to_move.is_valid_move(self, new_col, new_row):
    #         # Выполняем перемещение фигуры
    #         piece_to_move.move(self, new_col, new_row)
    #         return True
    #     else:
    #         return False
        


    # def move_piece(self, piece, new_col, new_row):
    #     # Проверяем, допустим ли такой ход
    #     if self.is_valid_move(piece, new_col, new_row):
    #         print("1!")
    #         # Получаем текущие координаты фигуры
    #         current_col, current_row = piece.get_piece_coordinates()
    #         print(f"Текущие координаты фигуры: ({current_col}, {current_row})")

    #         # Удаляем фигуру с текущей позиции
    #         self.remove_piece(piece)
            
    #         # Обновляем координаты фигуры
    #         piece.set_position(new_col, new_row)  # Уберите self из аргументов
    #         print(f"Новые координаты фигуры: ({new_col}, {new_row})")
            
    #         # Добавляем фигуру на новую позицию
    #         self.add_piece(piece, new_col, new_row)
            
    #         # Обновляем визуальное представление доски
    #         if self.board_gui:
    #             self.board_gui.update_board_visuals()

    # def remove_piece(self, piece):
    #     if piece in self.pieces:
    #         row, col = self.pieces[piece]
    #         self.board[row][col] = None
    #         del self.pieces[piece]


# test = GameLogic(None)
# test.initialize_board()
# board = test.board
# for row in board:
#     for elem in row:
#         print(elem,end=" ")
#     print()


# test = GameLogic(None)
# test.initialize_board()
# print(test.get_piece_at(0,1))

#ПРОВЕРКА MOVE_PIECE == TRUE
# test = GameLogic(None)
# test_piece = Piece("white",1,1)
# test.move_piece(test_piece,2,2)
# print(test_piece.get_piece_coordinates())
# print(test_piece.set_position(2,2))

#ПРОВЕРКА IS_VALID_MOVE  == TRUE
# test = GameLogic(None)
# test.initialize_board()
# test_piece = Pawn("white",6,3)
# print(test.is_valid_move(test_piece,5,3))