from django.db import models

class Ticket(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tickets/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
        ('archivado', 'Archivado')
    ], default='abierto')

    def __str__(self):
        return f'Ticket #{self.id} - {self.nombre_usuario}'