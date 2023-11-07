from piece import EmptyCell, King
# from board import ChessBoardGUI

class GameLogic:
    def __init__(self, board_gui):
        self.board_gui = board_gui


    def can_take(self, piece, piece_to_take):
        coordinates = piece_to_take.get_piece_coordinates()
        if coordinates in piece.movement():
            return True
        else:
            return False    


    def taking(self, piece, piece_is_taking):
        if self.can_take(piece, piece_is_taking):
            taken_coordinates = piece_is_taking.get_piece_coordinates()
            self.board_gui.remove_piece(piece)
            self.board_gui.remove_piece(piece_is_taking)
            target_coordinates = piece.get_piece_coordinates()
            self.board_gui.add_piece(piece, taken_coordinates[0], taken_coordinates[1])
            piece.set_position(taken_coordinates[0], taken_coordinates[1])
            self.board_gui.add_piece(EmptyCell(), target_coordinates[0], target_coordinates[1])
            self.board_gui.selected_piece = None

            # Смена текущего игрока
            if self.board_gui.current_player == "white":
                self.board_gui.current_player = "black"
            else:
                self.board_gui.current_player = "white"
        else:
            print("Cannot take this piece.")


    def find_king_coordinates(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board_gui.get_piece_at(row, col)
                if isinstance(piece, King) and piece.get_color() == color:
                    return (row, col)
        return None  

    # def check(self, piece):
    #     if self.board_gui.current_player == "white":
    #         color = "black"
    #     else:
    #         color = "white"
    #     king_coordinates = self.find_king_coordinates(color)
    #     print(king_coordinates)
    #     if king_coordinates in piece.movement():
    #         return True
    #     else:
    #         return False
        
    def check(self):
        if self.board_gui.current_player == "white": # take enemy color
            color = "black"  
        else:
            color = "white"
        king_coordinates = self.find_king_coordinates(color) # take enemy king coordinates 
        print(king_coordinates)
        for row in range(8):
            for col in range(8):
                piece = self.board_gui.board[row][col] # check every piece
                if piece is None:  
                    continue
                if isinstance(piece, EmptyCell):
                    continue
                if piece.get_color() != color: # if piece color different from king color
                    print(piece.movement())
                    if king_coordinates in piece.movement(): # check: can piece take king
                            return True
                    return False

