from tkinter import Button, Canvas, PhotoImage, Tk
from piece import Pawn, King, Knight, Bishop, Rook, Queen, Piece, EmptyCell
# from logic import GameLogic


class ChessBoardGUI:

    def __init__(self, root, board_logic):
        self.root = root
        self.root.title("Chess Board")
        self.board_logic = board_logic
        self.buttons = []  
        # self.button_images = []
        # self.active_images = []
        self.selected_piece = None
        self.current_player = "white"
        self.pieces = {}
        self.board = [[None for _ in range(8)] for _ in range(8)] # двухмерный массив
        # self.board_gui = board_guis
        self.current_player = "white"

        self.board_gui = None

        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.initialize_board_buttons()
        print("Selected piece -",self.selected_piece)


    # def piece_clicked(self, event, piece):
    #     if self.selected_piece is None:
    #         # Если еще не выбрана фигура, выберите ее
    #         self.selected_piece = piece
    #         print("selected piece -", self.selected_piece)
    #     else:
    #         # Если уже выбрана фигура
    #         if piece and piece.get_color() == self.selected_piece.get_color():
    #             # Если выбрана фигура того же цвета, перезапишите выбранную фигуру
    #             self.selected_piece = piece
    #             print("selected piece -", self.selected_piece)
    #         elif piece:
    #             # Если выбрана фигура другого цвета, выполните ход
    #             target_coordinates = piece.get_piece_coordinates()
    #             if self.selected_piece.move_piece(self,target_coordinates[0], target_coordinates[1]):
    #                 # Фигура перемещена на целевые координаты
    #                 self.selected_piece = None
    #                 self.current_player = "black" if self.current_player == "white" else "white"
    #                 print("selected piece -", self.selected_piece)
    #             else:
    #                 # Обработайте недопустимый ход (по желанию)
    #                 print("Invalid move")
    #         else:
    #             # Если нажата пустая клетка, обновите координаты выбранной фигуры
    #             target_coordinates = self.selected_piece.get_piece_coordinates()
    #             if self.selected_piece.move_piece(self, target_coordinates[0], target_coordinates[1]):
    #                 self.selected_piece = None
    #             else:
    #                 # Обработайте недопустимый ход (по желанию)
    #                 print("Invalid move")
    #                 print("selected piece -", self.selected_piece)

    #     self.update_board_visuals()

    # def find_empty_cells(self):
    #     empty_cells = []
    #     for row in range(8):
    #         for col in range(8):
    #             cell = self.get_piece_at(row, col)
    #             if isinstance(cell, EmptyCell):
    #                 empty_cells.append((row, col))
    #                 print(empty_cells)
    #     return empty_cells
    

    def piece_clicked(self, event, row, col):
        selected_piece = self.get_piece_at(row, col)  # Получить фигуру на выбранной клетке

        print("Selected piece -", selected_piece)
        
        if selected_piece and not isinstance(selected_piece, EmptyCell):  # Используйте явное сравнение с None
            if selected_piece.get_color() == self.current_player:
                self.selected_piece = selected_piece
                # print("Selected piece -", self.selected_piece.get_type())
        else:
            target_coordinates = (row, col)
            print(target_coordinates)  # Координаты выбранной пустой клетки
            if self.selected_piece:
                # Если есть выбранная фигура, попытайтесь выполнить ход
                if self.selected_piece.move(target_coordinates[0], target_coordinates[1]):
                    self.selected_piece = None
                    self.current_player = "black" if self.current_player == "white" else "white"
                    print("Selected piece - None")
                else:
                    print("Invalid move")
            else:
                print("No piece on this square")
            
        self.update_board_visuals()


    def initialize_board(self):
            # Расставляем начальные фигуры на доске
            for i in range(8):
                self.add_piece(Pawn("black", 1, i,self), 1, i)
                self.add_piece(Pawn("white",6,i,self),6, i)
            #Rook
            self.add_piece(Rook("black", 0, 0,self), 0, 0)
            self.add_piece(Rook("black", 0, 7,self), 0, 7)
            self.add_piece(Rook("white", 7, 0,self), 7, 0)
            self.add_piece(Rook("white", 7, 7,self), 7, 7)
            #Bishop
            self.add_piece(Bishop("black",0,2,self),0,2)
            self.add_piece(Bishop("black",0,5,self),0,5)
            self.add_piece(Bishop("white",7,2,self),7,2)
            self.add_piece(Bishop("white",7,5,self),7,5)
            #Knight
            self.add_piece(Knight("black",0,1,self),0,1)
            self.add_piece(Knight("black",0,6,self),0,6)
            self.add_piece(Knight("white",7,1,self),7,1)
            self.add_piece(Knight("white",7,6,self),7,6)
            #King
            self.add_piece(King("white",7,4,self),7,4)
            self.add_piece(King("black",0,4,self),0,4)
            # Queens
            self.add_piece(Queen("white",7,3,self),7,3)
            self.add_piece(Queen("black",0,3,self),0,3)
            # EmptyCell
            for row in range(2, 6):  # Это для центральной части доски
                for col in range(8):
                    empty_cell = EmptyCell(row, col, self)
                    empty_cell.set_value("empty")  # Установите значение пустой клетки
                    self.add_piece(empty_cell, row, col)

    def initialize_board_buttons(self):
        size = 50

        for i in range(8):
            row_buttons = []
            for j in range(8):
                x1, y1 = size * j, size * i
                color = "#C0C0C0" if (i + j) % 2 == 0 else "#808080"
                # piece = self.get_piece_at(i, j)
                button = Button(master=self.canvas, text="", bg=color)
                button.place(x=x1, y=y1, width=size, height=size)
                button.bind("<Button-1>", 
                            lambda event, row=i, col=j: self.piece_clicked(event, row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)
    

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
    
    
    def move(self, board_logic, new_row, new_col):
        # Ваша логика проверки допустимости хода
        if self.is_valid_move(board_logic, new_row, new_col):
            # Переместить фигуру на новую позицию
            self.remove_piece(self)
            self.set_position(new_row, new_col)
            self.add_piece(self,new_row,new_col)
            return True
        else:
            return False
        

    def set_position(self, new_row, new_col):
        # Установите новые координаты фигуры
        self.row = new_row
        self.col = new_col


    def remove_piece(self, piece):
        if piece in self.pieces:
            row, col = self.pieces[piece]
            self.board[row][col] = None
            del self.pieces[piece]


    def get_piece_at(self, row, col):
        return self.board[row][col]
    

    def add_piece(self, piece, row, col):
        self.pieces[piece] = (row, col)
        self.board[row][col] = piece


    # def update_board_visuals(self):
    #     size = 50

    #     for i in range(8):
    #         for j in range(8):
    #             x1, y1 = size * j, size * i
    #             color = "#C0C0C0" if (i + j) % 2 == 0 else "#808080"
    #             piece = self.get_piece_at(i, j)
    #             image_path = None

    #             if piece:
    #                 image_path = piece.get_image_path()

    #             button = self.buttons[i][j]
    #             button.config(text="", borderwidth=0)

    #             if image_path:
    #                 image = PhotoImage(file=image_path)
    #                 button.config(image=image)
    #                 button.image = image

    #                 # Сохраните ссылку на изображение в объекте фигуры
    #                 piece = self.get_piece_at(i, j)
    #                 if piece:
    #                     piece.set_image(image)
    #             else:
    #                 # Если нет изображения, очистите кнопку
    #                 button.config(image=None)


    #     self.root.update()

    def update_board_visuals(self):
        size = 50

        for i in range(8):
            row_buttons = []
            for j in range(8):
                x1, y1 = size * j, size * i
                color = "#C0C0C0" if (i + j) % 2 == 0 else "#808080"
                piece = self.get_piece_at(i, j)
                image_path = None  # Початкове значення для шляху зображення

                if piece:
                    image_path = piece.get_image_path()  # Отримати шлях до зображення для фігури

                button = Button(master=self.canvas, text="", bg=color)
                button.place(x=x1, y=y1, width=size, height=size)

                if image_path:
                    # Якщо є шлях до зображення, завантажте його і встановіть на кнопку
                    image = PhotoImage(file=image_path)
                    button.config(image=image)
                    button.image = image  # Збережіть посилання на зображення, щоб воно не було очищено сміттям

                # Прив'яжіть обробник кліку до кнопки
                button.bind("<Button-1>", 
                            lambda event, row=i, col=j: self.piece_clicked(event, row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)
    
#     # Проверка таблицы TEST
#     def print_board(self):
#         for row in range(8):
#             for col in range(8):
#                 piece = self.get_piece_at(row, col)
#                 if piece:
#                     if isinstance(piece, EmptyCell):
#                         print(f"Row: {row}, Col: {col}, Value: {piece.get_value()}")
#                     else:
#                         print(f"Row: {row}, Col: {col}, Piece: {piece.get_type()} ({piece.get_color()})")
#                 else:
#                     print(f"Row: {row}, Col: {col}, Empty")

# # TEST
# if __name__ == "__main__":
#     root = Tk()
#     board_logic = GameLogic(None)
#     chess_board = ChessBoardGUI(root, board_logic)
#     chess_board.initialize_board()
#     chess_board.print_board()
#     root.mainloop()



