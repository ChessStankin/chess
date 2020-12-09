from .models import ColorEnum, Player, Game, Move, Piece
from django.contrib.auth.models import User
import logging


def get_every_game_by_id(game_id: int) -> Game:
    game: Game = Game.objects.filter(id=game_id).first()
    if game is None:
        logging.warning(f'{game} is None, be careful')
    return game


def get_not_ended_game_by_id(game_id: int) -> Game:
    game: Game = Game.objects.filter(id=game_id).first()
    if game is None or game.is_ended == False:
        logging.warning(f'{game} is None or ended, be careful')
        return None
    return game


def get_bot() -> User:
    bot: User = User.objects.filter(username='bot').first()
    return bot


def create_player() -> Player:
    pass

