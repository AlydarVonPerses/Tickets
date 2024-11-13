from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm  # Debemos crear este formulario

# Vista para crear un nuevo ticket
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tickets:lista_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_ticket.html', {'form': form})

# Vista para mostrar todos los tickets
def lista_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/lista_tickets.html', {'tickets': tickets})
