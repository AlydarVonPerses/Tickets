from django.db import models

class Ticket(models.Model):
    ESTADOS = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
        ('archivado', 'Archivado'),
    ]
    
    nombre_usuario = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tickets/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='abierto')
    
    def __str__(self):
        return f"Ticket #{self.id} - {self.nombre_usuario}"
