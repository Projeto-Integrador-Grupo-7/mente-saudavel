from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionario, name='questionario'),
    path('questionario/<int:formulario_id>/', views.questionario, name='questionario'),
]