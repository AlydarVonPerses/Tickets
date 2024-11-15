from django.db import models

# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Prioridad
class Prioridad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Ticket
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
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Ticket #{self.id} - {self.nombre_usuario}'

# Modelo de Usuario (si quieres tener un perfil de usuario)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
