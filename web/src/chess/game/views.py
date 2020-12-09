from .models import ColorEnum, Player, Game, Move, Piece
import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User

# Create your views here.
def _get_random_color() -> ColorEnum:
    random_int: int = int(random.random())
    if random_int == 0:
        return ColorEnum.white
    else:
        return ColorEnum.black 


def _get_default_fen_position() -> str:
    return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'


def _get_bot_user() -> User:
    bot: User = User.objects.filter(username='bot').first()
    return bot


def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'game/test.html')


# remark need to create factory or builder 
def create_board(request: HttpRequest) -> HttpResponse:
    """
        Here is should be a simple button kinda like "Find game"
        Also creating new game => rederecting on new game page
    """
    if request.method == 'POST':
        color: ColorEnum = _get_random_color()
        user: User = request.user
        bot: User = _get_bot_user()
        player1: Player = Player(user, color)
        if color == ColorEnum.black:
            player2: Player = Player(bot, color=ColorEnum.white)
        else:
            player2: Player = Player(bot, color=ColorEnum.white)
        game: Game = Game(player1, player2, _get_default_fen_position(), False)
        player1.save()
        player2.save()
        game.save()


# each game contains unique id
def game_workflow(request: HttpRequest, game_id: int) -> HttpResponse:
    if request.method == 'POST':
        # does game exist or not ended?
        game: Game = Game.objects.filter(id=game_id).first()
        if game is None or game.is_ended == True:
            return HttpResponseNotFound()
      
        # get players for some tasks
        player1: Player = game.player1
        player2: Player = game.player2
        if player1 is None or player2 is None:
            return HttpResponseNotFound()
        # i'm planning to get fen and move from front
        fen_str: str = request.POST['fen']
        move_str: str = request.POST['move']
        # we need somehow to get move color
        color: str = ColorEnum.black
        player_maked_move: Player = None

        if player1.color == color:
            player_maked_move: Player = player1
        else:
            player_maked_move: Player = player2

        if player_maked_move is None:
            return HttpResponseNotFound()

        # so, we need to get move from this game, which belongs to player, who've maked move

        last_move: Move = Move.objects.filter(game_id=game.id, player_id=player_maked_move.id).order_by('-id').first()

        if last_move is not None:
            piece_id_last: Piece = last_move.piece_id_current
            move_str_last: str = last_move.move_str_current
        else:
            piece_id_last: Piece = None
            move_str_last: str = ''
        
        # now saving new move

        # is it default move?

        # is it promotion move?

        # is it checkmate?