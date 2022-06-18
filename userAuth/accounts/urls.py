from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginFunc, name='login'),
    path('logout/', views.logoutFunc, name='logout'),
    path('user/', views.funcUser, name='user'),
    path('accountSettings/', views.accountSettings, name='accountSettings'),
]
