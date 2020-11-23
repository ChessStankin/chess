from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import LoginForm, RegForm


def reg_page(request: HttpRequest) -> HttpResponse:
    context = {'reg_form': RegForm()}
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid() and reg_form.passwords_equal():
            username = reg_form.data['username']
            password = reg_form.data['password']
            email = reg_form.data['email']
            if not User.objects.filter(Q(username=username) | Q(email=email)).exists():
                User.objects.create_user(username, email, password)
                return redirect('/account/login/')
        else:
            context['reg_form'] = reg_form
    return render(request, 'account/reg_page.html', context)


def login_page(request: HttpRequest) -> HttpResponse:
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.data['username']
            password = login_form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            context['login_form'] = login_form
    return render(request, 'account/login_page.html', context)


def logout_func(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        logout(request)
        return HttpResponse('Ok')
    return HttpResponse('Bad')


@login_required
def profile_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/profile_page.html')