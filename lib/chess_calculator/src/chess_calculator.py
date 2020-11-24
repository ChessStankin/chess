import stockfish

from stockfish import Stockfish

stockfish = Stockfish("/Users/bak-h/stockfish/stockfish64")
#chessEngine = Engine('./stockfish_64', param={'Threads': 5, 'Ponder': None})

def get_next_move(fen: str) -> str:
    return stockfish.get_best_move(fen)


def is_best_move(move: str) -> bool:
        return stockfish.is_move_correct(str)