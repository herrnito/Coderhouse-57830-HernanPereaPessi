# from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "pasteleria"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("torta/list", login_required(views.torta_list), name="torta_list"),
    path("cliente/list", login_required(views.cliente_list), name="cliente_list"),
    path("pedido/list", login_required(views.pedido_list), name="pedido_list"),
    path("torta/create", login_required(views.torta_create), name="torta_create"),
    path("pedido/create", login_required(views.pedido_create), name="pedido_create"),
    path("cliente/create", login_required(views.cliente_create), name="cliente_create"),
    path("torta_list/detail/<int:pk>", login_required(views.torta_list_detail), name='torta_list_detail'),
    path("cliente_list/detail/<int:pk>", login_required(views.cliente_list_detail), name='cliente_list_detail'),
    path("pedido_list/detail/<int:pk>", login_required(views.pedido_list_detail), name='pedido_list_detail'),
    path("torta/update/<int:pk>", login_required(views.torta_update), name="torta_update"),
    path("cliente/update/<int:pk>", login_required(views.cliente_update), name="cliente_update"),
    path("pedido/update/<int:pk>", login_required(views.pedido_update), name="pedido_update"),
    path("torta/delete/<int:pk>", login_required(views.torta_delete), name="torta_delete"),
    path("cliente/delete/<int:pk>", login_required(views.cliente_delete), name="cliente_delete"),
    path("pedido/delete/<int:pk>", login_required(views.pedido_delete), name="pedido_delete"),

    
]   
