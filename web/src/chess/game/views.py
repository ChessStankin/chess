from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'game/test.html')

