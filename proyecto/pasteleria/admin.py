from django.contrib import admin
from .models import Cliente, Torta, Pedido
# from . import models


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono", "email")
    search_fields = ("nombre", "direccion", "telefono", "email")
    ordering = ("nombre", "telefono")

@admin.register(Torta)
class TortaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "torta", "cantidad", "estado", "fecha_pedido")
    list_filter = ("estado", "fecha_pedido")
    search_fields = ("cliente__nombre", "torta__nombre")
    date_hierarchy = "fecha_pedido"