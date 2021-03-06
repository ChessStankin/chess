from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import LoginForm, RegForm, EmailForm, PasswordEditForm
from .models import AuthJWT
from types import FunctionType
from random import randint


def check_jwt(function: FunctionType):
    def inner(request, *args, **kwargs):
        jwt_cookie = request.COOKIES.get('jwt')
        try:
            jwt_model = AuthJWT.objects.get(user=request.user)
            if jwt_model.is_expired() or jwt_cookie != jwt_model.token:
                logout(request)
                messages.add_message(request, messages.ERROR, "Сессия устарела.")
                return redirect('/account/login/')
            return function(request, *args, **kwargs)
        except AuthJWT.DoesNotExist:
            logout(request)
            messages.add_message(request, messages.ERROR, "Сессия устарела.")
            return redirect('/account/login/')
    return inner


def jwt_authenticate(request, user):
    try:
        jwt_model = AuthJWT.objects.get(user=user)
        jwt_model.refresh()
    except AuthJWT.DoesNotExist:
        jwt_model = AuthJWT.objects.create(user=user)
    response = redirect('profile')
    remember_me = request.POST.get('remember_me')
    if remember_me is None:
        response.set_cookie('jwt', jwt_model.token, samesite='Lax')
    else:
        response.set_cookie('jwt', jwt_model.token, samesite='Lax', max_age=604800)
    return response


def reg_page(request: HttpRequest) -> HttpResponse:
    context = {'reg_form': RegForm()}
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "Вы авторизированы.")
        return redirect('profile')

    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        context['reg_form'] = reg_form
        if reg_form.is_valid():
            if reg_form.passwords_equal():
                username = reg_form.data['username']
                password = reg_form.data['password']
                email = reg_form.data['email']
                if not User.objects.filter(Q(username=username) | Q(email=email)).exists():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    response = jwt_authenticate(request, user)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.add_message(request, messages.SUCCESS,
                                         "Вы зарегистрировались!")
                    return response
                else:
                    messages.add_message(request, messages.ERROR,
                                         "Пользователь с такими данными существует.")
            else:
                messages.add_message(request, messages.ERROR, "Пароли не совпадают.")
    return render(request, 'account/reg_page.html', context)


def login_page(request: HttpRequest) -> HttpResponse:
    context = {'login_form': LoginForm()}
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "Вы авторизированы.")
        return redirect('profile')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        context['login_form'] = login_form
        if login_form.is_valid():
            username_or_email = login_form.data['username_or_email']
            password = login_form.data['password']
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                user = authenticate(email=username_or_email, password=password)
            if user is not None:
                response = jwt_authenticate(request, user)
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Авторизация выполнена.")
                return response
        messages.add_message(request, messages.ERROR, "Некорректные данные.")
    return render(request, 'account/login_page.html', context)


def logout_func(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "Вы вышли из аккаунта.")
        return HttpResponse('Ok')
    return HttpResponse('Bad')


@login_required
@check_jwt
def profile_page(request: HttpRequest) -> HttpResponse:
    context = {
        'email_form': EmailForm(initial={'email': request.user.email}),
        'pwd_form': PasswordEditForm(),
        'wins': randint(10, 1000),
        'losses': randint(10, 1000),
    }
    context['wl'] = round(context['wins'] / context['losses'], 2)

    if request.method == 'POST':
        if 'email' in request.POST:
            email_form = EmailForm(request.POST)
            context['email_form'] = email_form
            if email_form.is_valid():
                new_email = email_form.data['email']
                if new_email != request.user.email:
                    if not User.objects.filter(email=new_email).exists():
                        user = request.user
                        user.email = new_email
                        user.save()
                        messages.add_message(request, messages.SUCCESS,
                                             "Привязанная почта изменена.")
                        return redirect('profile')
                    else:
                        messages.add_message(request, messages.ERROR,
                                             "Данная почта привязана к другому аккаунту.")
                else:
                    messages.add_message(request, messages.WARNING,
                                         "Данная почта совпадает со старой.")

        if 'current_password' in request.POST:
            pwd_form = PasswordEditForm(request.POST)
            context['pwd_form'] = pwd_form
            if pwd_form.is_valid():
                if request.user.check_password(pwd_form.data['current_password']):
                    if pwd_form.is_password_new():
                        if pwd_form.passwords_equal():
                            request.user.set_password(pwd_form.data['new_password'])
                            request.user.save()
                            update_session_auth_hash(request, request.user)
                            messages.add_message(request, messages.SUCCESS,
                                                 "Пароль изменен.")
                            return redirect('profile')
                        else:
                            messages.add_message(request, messages.ERROR,
                                                 "Пароли не совпадают.")
                    else:
                        messages.add_message(request, messages.WARNING,
                                             "Новый пароль совпадает со старым.")
                else:
                    messages.add_message(request, messages.ERROR,
                                         "Неправильный текущий пароль")

    return render(request, 'account/profile_page.html', context)
