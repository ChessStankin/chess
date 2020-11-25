import stockfish
import os
dir_stockfish = os.path.abspath('stockfish64.exe')
from stockfish import Stockfish
stockfish = Stockfish(dir_stockfish)

def get_next_move(fen1,fen2: str) -> str:
    stockfish.set_position([fen1, fen2])
    return stockfish.get_best_move()

def is_best_move(move: str) -> bool:
    return stockfish.is_move_correct(move)
