import stockfish
import os
import platform

dir_stockfishWin = os.path.abspath('stockfish64.exe')
dir_stockfishLin = os.path.abspath('stockfish')

stockfish = stockfish.Stockfish(dir_stockfishWin) 

if platform.system() == "Linux":
    stockfish = stockfish.Stockfish(dir_stockfishLin)
    
def get_next_move(fen1,fen2: str) -> str:
    stockfish.set_position([fen1, fen2])
    return stockfish.get_best_move()

def is_best_move(move: str) -> bool:
    return stockfish.is_move_correct(move)
