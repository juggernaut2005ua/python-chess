from tkinter import Button, Canvas, PhotoImage, Tk
from piece import Pawn, King, Knight, Bishop, Rook, Queen, EmptyCell



class ChessBoardGUI:

    def __init__(self, root, board_logic):
        self.root = root
        self.root.title("Chess Board")
        self.board_logic = board_logic
        self.buttons = []  
        self.selected_piece = None
        self.pieces = {}
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.current_player = "white"

        self.board_gui = None

        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.initialize_board_buttons()
    

    def piece_clicked(self, event, row, col):
        selected_piece = self.get_piece_at(row, col)
        
        if selected_piece and not isinstance(selected_piece, EmptyCell):
            if selected_piece.get_color() == self.current_player:
                self.selected_piece = selected_piece

                if self.board_logic.check():
                    print("Check")
            else:
                print(self.selected_piece, selected_piece)
                self.board_logic.taking(self.selected_piece, selected_piece)
        else:
            target_coordinates = (row, col)
            if self.selected_piece:
                if self.selected_piece.move(target_coordinates[0], target_coordinates[1]):
                    self.selected_piece = None
                    self.current_player = "black" if self.current_player == "white" else "white"
                else:
                    print("Invalid move")
            else:
                print("No piece on this square")

        self.update_board_visuals()



    def initialize_board(self):

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
            for row in range(2, 6):  
                for col in range(8):
                    empty_cell = EmptyCell(row, col, self)
                    empty_cell.set_value("empty")
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
    
    def move(self, board_logic, new_row, new_col):
        if self.is_valid_move(board_logic, new_row, new_col):
            self.remove_piece(self)
            self.set_position(new_row, new_col)
            self.add_piece(self,new_row,new_col)
            return True
        else:
            return False
        

    def set_position(self, new_row, new_col):
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
                image_path = None  

                if piece:
                    image_path = piece.get_image_path()  

                button = Button(master=self.canvas, text="", bg=color)
                button.place(x=x1, y=y1, width=size, height=size)

                if image_path:
                    
                    image = PhotoImage(file=image_path)
                    button.config(image=image)
                    button.image = image  

                button.bind("<Button-1>", 
                            lambda event, row=i, col=j: self.piece_clicked(event, row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)

# root = Tk()
# test = ChessBoardGUI(root,None)
# test.initialize_board()
# print(test.board)