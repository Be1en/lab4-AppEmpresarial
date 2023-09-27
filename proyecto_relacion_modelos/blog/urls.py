from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('', views.index, name='index'),
    path('lista_mario/', views.lista_mario, name='lista_mario'),
    path('lista_ton/', views.lista_ton, name='lista_ton')
]
