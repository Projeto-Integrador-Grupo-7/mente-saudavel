from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionario, name='questionario'),
    path('cadastro/', views.cadastro_questionario, name='cadastro_questionario'),
]