from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
   path('listar/', views.listar_tickets, name='listar_tickets'),
   path('crear/', views.crear_ticket, name='crear_ticket'),
   path('', views.menu, name='menu'),
   path('login/', views.login, name='login'),
   path('listar/admin/', views.listar_tickets_admin, name='listar_tickets_admin'),
   path('listar/tecnico/', views.listar_tickets_tecnico, name='listar_tickets_tecnico'),
   path('editar/<int:ticket_id>/', views.editar_ticket, name='editar_ticket'),
   path('ver/<int:ticket_id>/', views.ver_ticket, name='ver_ticket'),
   path('eliminar/<int:ticket_id>/', views.eliminar_ticket, name='eliminar_ticket'),
   path('actualizar_estado/<int:ticket_id>/', views.actualizar_estado_ticket, name='actualizar_estado_ticket'),
    # Para el administrador
    path('ticket/ver/admin/<int:ticket_id>/', views.ver_ticket_admin, name='ver_ticket_admin'),
    
    # Para el técnico
    path('ticket/ver/tecnico/<int:ticket_id>/', views.ver_ticket_tecnico, name='ver_ticket_tecnico'),
    
    #Acceso mediante urls
     # Ruta para acceso del administrador
    path('admin/<str:password>/', views.admin_tickets, name='admin_tickets'),
    
    # Ruta para acceso del técnico
    path('tecnico/<str:password>/', views.tecnico_tickets, name='tecnico_tickets'),

]
