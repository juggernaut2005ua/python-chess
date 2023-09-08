import functools
from tkinter import Button, Canvas, PhotoImage
from piece import Piece


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



