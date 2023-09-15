from piece import Pawn, King, Knight, Bishop, Rook, Queen, Piece, EmptyCell
# from board import ChessBoardGUI

class GameLogic:
    def __init__(self, board_gui):
        self.pieces = {}
        self.board_gui = board_gui
        self.current_player = "white"


    def can_take(self, piece, piece_to_take):
        coordinates = piece_to_take.get_piece_coordinates()
        if coordinates in piece.movement():
            return True
        else:
            return False    


    def taking(self, piece, piece_is_taking):
        if self.can_take(piece, piece_is_taking):
            # Получаем координаты фигуры, которую будем брать
            taken_coordinates = piece_is_taking.get_piece_coordinates()

            # Удаляем фигуру, которую мы берем, с ее текущей позиции
            self.board_gui.remove_piece(piece)

            # Удаляем фигуру, которая была взята, с ее текущей позиции
            self.board_gui.remove_piece(piece_is_taking)

            # Получаем координаты фигуры, которой будет сделан ход
            target_coordinates = piece.get_piece_coordinates()

            # Перемещаем фигуру, которая берет, на позицию фигуры, которая была взята
            self.board_gui.add_piece(piece, taken_coordinates[0], taken_coordinates[1])

            # Обновляем координаты фигуры, которая берет
            piece.set_position(taken_coordinates[0], taken_coordinates[1])

            # Помещаем пустую клетку (EmptyCell) на старую позицию фигуры, которая берет
            self.board_gui.add_piece(EmptyCell(), target_coordinates[0], target_coordinates[1])

            self.board_gui.selected_piece = None

            # Смена текущего игрока
            if self.board_gui.current_player == "white":
                self.board_gui.current_player = "black"
            else:
                self.board_gui.current_player = "white"
        else:
            print("Cannot take this piece.")

