# from django.contrib import admin
from django.urls import path
from . import views

app_name = "pasteleria"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("torta/list", views.torta_list, name="torta_list"),
    path("cliente/list", views.cliente_list, name="cliente_list"),
    path("pedido/list", views.pedido_list, name="pedido_list"),
    path("torta/create", views.torta_create, name="torta_create"),
    path("pedido/create", views.pedido_create, name="pedido_create"),
    path("cliente/create", views.cliente_create, name="cliente_create"),
    path("torta_list/detail<int:pk>", views.torta_list_detail, name='torta_list_detail'),
    path("cliente_list/detail<int:pk>", views.cliente_list_detail, name='cliente_list_detail'),
    # path("torta/update<int:pk>", views.torta_update, name="torta_update"),

]
