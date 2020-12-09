from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ColorEnum():
    white: str = "white"
    black: str = "black"
    

class PieceEnum():
    white_king: str = "white_king"
    white_quenn: str = "white_quenn"
    white_rook: str = "white_rook"
    white_bishop: str = "white_bishop"
    white_knight: str = "white_knight"
    white_pawn: str = "white_pawn"
    black_king: str = "black_king"
    black_quenn: str = "black_quenn"
    black_rook: str = "black_rook"
    black_bishop: str = "black_bishop"
    black_knight: str = "black_knight"
    black_pawn: str = "black_pawn" 


class Player(models.Model):
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    color: models.CharField = models.CharField(max_length=16, default="")


    def __str__(self) -> str:
        return f"<{self.user_id=},\n{self.color=}>"


    def __repr__(self) -> str:
        return self.__str__()


class Game(models.Model):
    player1: models.ForeignKey = models.ForeignKey(Player, related_name="+", on_delete=models.CASCADE)
    player2: models.ForeignKey = models.ForeignKey(Player, related_name="+", on_delete=models.CASCADE)
    current_fen_position: models.CharField = models.CharField(max_length=256, default="") 
    is_ended: models.BooleanField = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"<{self.player1=},\n{self.player2=},\n{self.current_fen_position=},\n{self.is_ended=}>"


    def __repr__(self) -> str:
        return self.__str__()


class Piece(models.Model):
    color: models.CharField = models.CharField(max_length=16)
    piece_type: models.CharField = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f"<{self.color=},\n{self.piece_type=}>"


    def __repr__(self) -> str:
        return self.__str__()


class Move(models.Model):
    game_id: models.ForeignKey = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_id: models.ForeignKey = models.ForeignKey(Player, on_delete=models.CASCADE)
    piece_id_last: models.ForeignKey = models.ForeignKey(Piece, related_name="+", on_delete=models.CASCADE)
    piece_id_current: models.ForeignKey = models.ForeignKey(Piece, related_name="+", on_delete=models.CASCADE)
    from_square: models.CharField = models.CharField(max_length=16)
    to_square: models.CharField = models.CharField(max_length=16)
    is_promotion_move: models.BooleanField = models.BooleanField(default=False)
    move_str_last: models.CharField = models.CharField(max_length=16)
    move_str_current: models.CharField = models.CharField(max_length=16)


    def __str__(self) -> str:
        return f"<{self.game_id=},\n{self.player_id=},\n{self.piece_id_last=},\n{self.piece_id_current=},\n{self.from_square=},\n{self.to_square=},\n{self.is_promotion_move=},\n{self.move_str_last=},\n{self.move_str_current=}>"


    def __repr__(self) -> str:
        return self.__str__()