# tickets/urls.py
from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('listar/', views.lista_tickets, name='lista_tickets'),
]
