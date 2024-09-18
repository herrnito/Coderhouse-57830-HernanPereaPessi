from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Torta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    torta = models.ForeignKey(Torta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])

    def __str__(self):
        return f'Pedido de {self.cliente.nombre}'
    
# class ProductoCategoria(models.Model):
#     nombre = models.CharField(max_length=100, unique=True)
#     descripcion = models.TextField(blank=True, null=True)

#     def __str__(self) -> str:
#         return self.nombre
    
#     class Meta:
#         verbose_name = "Categoria de producto"
#         verbose_name_plural = "Categorias de productos"