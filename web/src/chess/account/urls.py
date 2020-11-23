from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('reg/', views.reg_page, name='reg'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_func, name='logout')
]
