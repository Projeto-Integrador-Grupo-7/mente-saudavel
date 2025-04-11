from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='login_usuario'),
    path('logout', views.logout_usuario, name='logout_usuario'),
]