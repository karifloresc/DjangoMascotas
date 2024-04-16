from django.urls import path
from . import views
from core.controlador import registroLogin

urlpatterns = [
    path('',views.home,name="home"),
    path('register/', registroLogin.register, name="register"),
    path('login/', registroLogin.loginpage, name='login' ),
    path('logout/', registroLogin.logoutpage, name="logout")
]