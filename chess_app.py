from tkinter import Tk
from logic import GameLogic
from board import ChessBoardGUI
from piece import Piece

if __name__ == "__main__":
    root = Tk()
    game_logic = GameLogic(None)
    chess_board_gui = ChessBoardGUI(root, game_logic)
    # game_logic.board_gui = chess_board_gui  # Установите board_gui
    chess_board_gui.initialize_board()
    chess_board_gui.update_board_visuals()
    root.mainloop()
