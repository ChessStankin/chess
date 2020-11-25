from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'game/test.html')


def create_board(request: HttpRequest) -> HttpResponse:
    """
        Here is should be a simple button kinda like "Find game"
        Also creating new game => rederecting on new game page
    """
    pass

# we need to keep moves sequence
# need to keep fen
# need to keep player1
# need to keep player2
def game_workflow(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # 1. we should save move
        pass