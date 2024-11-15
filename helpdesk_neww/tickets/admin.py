from django.contrib import admin
from .models import Categoria, Prioridad, Ticket, Usuario

admin.site.register(Categoria)
admin.site.register(Prioridad)
admin.site.register(Ticket)
admin.site.register(Usuario)
