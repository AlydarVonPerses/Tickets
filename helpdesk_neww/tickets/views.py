from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Usuario, Categoria, Prioridad
from .forms import TicketForm
from django.urls import reverse
from django.http import HttpResponseForbidden

def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets.html', {'tickets': tickets})

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.estado = 'abierto'  # Estado por defecto como "abierto"
            ticket.save()
            return redirect('tickets:listar_tickets')  # Redirige al listado de tickets tras la creación
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_tickets.html', {'form': form})

def menu(request):
    return render(request, 'tickets/menu.html')

def login(request):
    if request.method == "POST":
        nombre_usuario = request.POST.get('nombre_usuario')
        rol = request.POST.get('rol')
        
        # Validar usuario y rol (esto puede personalizarse según tus reglas)
        usuario = Usuario.objects.filter(nombre=nombre_usuario).first()
        
        if usuario:
            if rol == "administrador":
                return redirect(reverse('tickets:listar_tickets_admin'))
            elif rol == "tecnico":
                return redirect(reverse('tickets:listar_tickets_tecnico'))
        else:
            return render(request, 'tickets/menu.html', {'error': 'Usuario no válido.'})
    return redirect('tickets:menu')

def listar_tickets_admin(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets_admin.html', {'tickets': tickets})

def listar_tickets_tecnico(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets_tecnico.html', {'tickets': tickets})

def editar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    # Obtener todas las categorías y prioridades
    categorias = Categoria.objects.all()
    prioridades = Prioridad.objects.all()

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets:listar_tickets_admin')  # Redirigir a la lista de tickets para el administrador
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'tickets/editar_ticket.html', {
        'form': form,
        'ticket': ticket,
        'categorias': categorias,  # Pasar las categorías al contexto
        'prioridades': prioridades  # Pasar las prioridades al contexto
    })

def ver_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/ver_ticket.html', {
        'ticket': ticket,
    })
def eliminar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('tickets:listar_tickets_admin')  # Cambiar 'listar_admin' por 'listar_tickets_admin'

def actualizar_estado_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        # Aquí tomamos el estado del formulario enviado
        nuevo_estado = request.POST.get('estado')
        
        if nuevo_estado in ['abierto', 'cerrado', 'en proceso']:  # Asegúrate de que el estado sea uno válido
            ticket.estado = nuevo_estado
            ticket.save()

        return redirect('tickets:listar_tickets_tecnico')
    
    # Si el método no es POST, solo mostramos el formulario
    return render(request, 'tickets/actualizar_estado_ticket.html', {'ticket': ticket})

# Para el administrador
def ver_ticket_admin(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/ver_ticket_admin.html', {'ticket': ticket})

# Para el técnico
def ver_ticket_tecnico(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/ver_ticket_tecnico.html', {'ticket': ticket})

# Contraseñas predefinidas 
PASSWORD_ADMIN = "admin123"

def admin_tickets(request, password):
    if password != PASSWORD_ADMIN:
        return HttpResponseForbidden("Acceso denegado. Contraseña incorrecta.")

    tickets = Ticket.objects.all()  # Todos los tickets para el administrador
    return render(request, 'tickets/listar_tickets_admin.html', {'tickets': tickets})

PASSWORD_TECNICO = "tecnico123"

def tecnico_tickets(request, password):
    if password != PASSWORD_TECNICO:
        return HttpResponseForbidden("Acceso denegado. Contraseña incorrecta.")

    tickets = Ticket.objects.all()  # Filtrar tickets si es necesario
    return render(request, 'tickets/listar_tickets_tecnico.html', {'tickets': tickets})