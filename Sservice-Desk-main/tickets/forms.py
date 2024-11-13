from django import forms
from .models import Ticket

class FormularioTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['nombre_usuario', 'descripcion', 'imagen']
