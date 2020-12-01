from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import LoginForm, RegForm


def reg_page(request) -> HttpResponse:
    context = {'reg_form': RegForm()}
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "Вы авторизированы.")
        return redirect('/account/profile/')

    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        context['reg_form'] = reg_form
        if reg_form.is_valid():
            if reg_form.passwords_equal():
                username = reg_form.data['username']
                password = reg_form.data['password']
                email = reg_form.data['email']
                if not User.objects.filter(Q(username=username) | Q(email=email)).exists():
                    user = User.objects.create_user(username, email, password)
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS,
                                         "Вы зарегистрировались!")
                    return redirect('/account/profile/')
                else:
                    messages.add_message(request, messages.ERROR,
                                         "Пользователь с такими данными существует.")
            else:
                messages.add_message(request, messages.ERROR, "Пароли не совпадают.")
    return render(request, 'account/reg_page.html', context)


def login_page(request: HttpRequest) -> HttpResponse:
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        context['login_form'] = login_form
        if login_form.is_valid():
            username = login_form.data['username']
            password = login_form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    return render(request, 'account/login_page.html', context)


def logout_func(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        logout(request)
        return HttpResponse('Ok')
    return HttpResponse('Bad')


@login_required
def profile_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/profile_page.html')