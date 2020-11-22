from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout, authenticate, login


def test(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/test.html')


def login_page(request: HttpRequest):
    user = authenticate(request, username='username', password='password')
    if user is not None:
        login(request, user)


def logout_func(request: HttpRequest):
    logout(request)
