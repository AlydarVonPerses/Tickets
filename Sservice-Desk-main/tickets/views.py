from django.shortcuts import render, redirect
from .models import Ticket
from .forms import FormularioTicket

def crear_ticket(request):
    if request.method == 'POST':
        formulario = FormularioTicket(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('tickets:lista_tickets')
    else:
        formulario = FormularioTicket()
    return render(request, 'crear_ticket.html', {'formulario': formulario})

def lista_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'lista_tickets.html', {'tickets': tickets})

def actualizar_estado(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.estado = request.POST.get('estado')
        ticket.save()
        return redirect('tickets:lista_tickets')
    return render(request, 'actualizar_estado.html', {'ticket': ticket})

def archivar_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.estado = 'archivado'
    ticket.save()
    return redirect('tickets:lista_tickets')

def obtener_rol(request):
    if 'rol' in request.GET:
        return request.GET['rol']
    return 'tecnico'  # Si no se pasa un parámetro, asignar como técnico


def archivar_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.estado = 'archivado'
    ticket.save()
    return redirect('tickets:lista_tickets')



