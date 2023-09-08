import functools
from tkinter import Button, Canvas, PhotoImage
from piece import Pawn, King, Knight, Bishop, Rook, Queen, Piece


class ChessBoardGUI:
    def __init__(self, root, board_logic):
        self.root = root
        self.root.title("Chess Board")
        self.board_logic = board_logic
        self.buttons = []  
        # self.button_images = []
        self.active_images = []
        self.selected_piece = None
        self.current_player = "white"
        self.pieces = {}

        self.board_gui = None

        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.initialize_board_buttons()
        print("Selected piece -",self.selected_piece)

    def piece_clicked(self, event, piece):
        if self.selected_piece is None:
            # Если еще не выбрана фигура, выберите ее
            self.selected_piece = piece
        else:
            # Если уже выбрана фигура
            if piece and piece.get_color() == self.selected_piece.get_color():
                # Если выбрана фигура того же цвета, перезапишите выбранную фигуру
                self.selected_piece = piece
            elif piece:
                # Если выбрана фигура другого цвета, выполните ход
                target_coordinates = piece.get_piece_coordinates()
                if self.selected_piece.move_piece(target_coordinates[0], target_coordinates[1]):
                    # Фигура перемещена на целевые координаты
                    self.selected_piece = None
                    self.current_player = "black" if self.current_player == "white" else "white"
                else:
                    # Обработайте недопустимый ход (по желанию)
                    print("Invalid move")
            else:
                # Если нажата пустая клетка, обновите координаты выбранной фигуры
                target_coordinates = self.selected_piece.get_piece_coordinates()
                if self.selected_piece.move_piece(self, target_coordinates[0], target_coordinates[1]):
                    self.selected_piece = None
                else:
                    # Обработайте недопустимый ход (по желанию)
                    print("Invalid move")

        self.update_board_visuals()



    def initialize_board_buttons(self):
        size = 50

        for i in range(8):
            row_buttons = []
            for j in range(8):
                x1, y1 = size * j, size * i
                color = "#C0C0C0" if (i + j) % 2 == 0 else "#808080"
                piece = self.board_logic.get_piece_at(i, j)
                
                
                def click_handler(event, i=i, j=j):
                    return self.piece_clicked(event, self.board_logic.get_piece_at(i, j))
                
                button = Button(master=self.canvas, text="", bg=color)
                button.place(x=x1, y=y1, width=size, height=size)
                button.bind("<Button-1>", click_handler)
                row_buttons.append(button)
            self.buttons.append(row_buttons)


    def entered(self, event, x, y):
        piece = self.board_logic.get_piece_at(x, y)
            
        if piece:
            piece_info = f"Type: {piece.get_type()}, Color: {piece.get_color()}"
            piece_cootdinates = f"xy{piece.get_piece_coordinates()}"
            print(piece_cootdinates)
            print(piece_info)
        else:
            print("No piece on this square")

        return piece
    
    def is_valid_move(self, piece_to_move, new_col, new_row):
        for piece, (col, row) in self.pieces.items():
            if col == new_col and row == new_row:
                return False
        
        piece_type = piece_to_move.get_type()
        current_row, current_col = piece_to_move.get_piece_coordinates()
        piece_color = piece_to_move.get_color()

        if piece_type == "Queen":
            # Проверка вертикальных и горизонтальных ходов, аналогично ладье
            if current_col == new_col or current_row == new_row:
                # Проверка наличия фигур на пути
                if current_col == new_col:
                    min_row, max_row = min(current_row, new_row), max(current_row, new_row)
                    for row in range(min_row + 1, max_row):
                        if self.get_piece_at(row, current_col):
                            return False
                else:
                    min_col, max_col = min(current_col, new_col), max(current_col, new_col)
                    for col in range(min_col + 1, max_col):
                        if self.get_piece_at(current_row, col):
                            return False
            # Проверка диагональных ходов, аналогично слону
            elif abs(current_col - new_col) == abs(current_row - new_row):
                col_step = 1 if new_col > current_col else -1
                row_step = 1 if new_row > current_row else -1
                col, row = current_col + col_step, current_row + row_step
                while col != new_col:
                    if self.get_piece_at(row, col):
                        return False
                    col += col_step
                    row += row_step
            else:
                return False
        elif piece_type == "Rook":
            if current_col == new_col or current_row == new_row:
                # Проверка наличия фигур на пути
                if current_col == new_col:
                    min_row, max_row = min(current_row, new_row), max(current_row, new_row)
                    for row in range(min_row + 1, max_row):
                        if self.get_piece_at(row, current_col):
                            return False
                else:
                    min_col, max_col = min(current_col, new_col), max(current_col, new_col)
                    for col in range(min_col + 1, max_col):
                        if self.get_piece_at(current_row, col):
                            return False
        elif piece_type == "Bishop":
            if abs(current_col - new_col) == abs(current_row - new_row):
                col_step = 1 if new_col > current_col else -1
                row_step = 1 if new_row > current_row else -1
                col, row = current_col + col_step, current_row + row_step
                while col != new_col:
                    if self.get_piece_at(row, col):
                        return False
                    col += col_step
                    row += row_step
            else:
                return False
            
        elif piece_type == "Pawn":
            if piece_color == "white":
                for other_piece, (col, row) in self.pieces.items():
                    if col == new_col and row == current_row + 1:
                        return False
            for other_piece, (col, row) in self.pieces.items():
                if col == new_col and row == current_row - 1:
                    return False
                
        elif piece_type == "Knight":
            moves = [
            (current_col + 1, current_row - 2), (current_col + 2, current_row - 1),
            (current_col + 2, current_row + 1), (current_col + 1, current_row + 2),
            (current_col - 1, current_row + 2), (current_col - 2, current_row + 1),
            (current_col - 2, current_row - 1), (current_col - 1, current_row - 2)
            ]
        # Проверяем, является ли новая позиция одной из возможных позиций коня
            if (new_col, new_row) in moves:
                return True
        elif piece_type == "King":
            # Проверка возможных ходов короля
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
    
    def move(self, board_logic, new_col, new_row):
        # Ваша логика проверки допустимости хода
        if self.is_valid_move(board_logic, new_col, new_row):
            # Переместить фигуру на новую позицию
            self.set_position(new_col, new_row)
            return True
        else:
            return False
        
    def set_position(self, new_col, new_row):
        # Установите новые координаты фигуры
        self.col = new_col
        self.row = new_row

    
    def move_piece(self, piece_to_move, new_col, new_row):
        # Проверяем, допустим ли такой ход
        if piece_to_move.is_valid_move(self, new_col, new_row):
            # Выполняем перемещение фигуры
            piece_to_move.move(self, new_col, new_row)
            return True
        else:
            return False

    def update_board_visuals(self):
        # Создать словарь для хранения объектов PhotoImage по пути к изображению
        image_cache = {}
        
        for i in range(8):
            for j in range(8):
                piece = self.board_logic.get_piece_at(i, j)
                if piece:
                    image_path = piece.get_image_path()
                    
                    # Попробовать получить изображение из кеша
                    if image_path in image_cache:
                        image = image_cache[image_path]
                    else:
                        # Если изображение ещё не в кеше, создать его и добавить в кеш
                        image = PhotoImage(file=image_path)
                        image_cache[image_path] = image
                    
                    self.buttons[i][j].config(image=image, text="", borderwidth=0)
                    self.buttons[i][j].image = image
                else:
                    self.buttons[i][j].config(image="", text="", borderwidth=0)

        # Обновить все кнопки
        self.root.update()



