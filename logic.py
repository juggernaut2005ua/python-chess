from piece import Pawn, King, Knight, Bishop, Rook, Queen, Piece
from board import ChessBoardGUI

class GameLogic:
    def __init__(self, board_gui):
        self.pieces = {}
        self.board = [[None for _ in range(8)] for _ in range(8)] # двухмерный массив
        self.board_gui = board_gui
        self.current_player = "white"
