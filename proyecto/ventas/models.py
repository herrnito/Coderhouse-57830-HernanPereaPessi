from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    celular = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self) -> str:
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("pasteleria.Torta", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveBigIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-fecha_venta']
    


    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)



