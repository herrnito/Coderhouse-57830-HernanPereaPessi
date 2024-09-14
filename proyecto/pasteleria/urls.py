# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("torta/list", views.torta_list),
    path("cliente/list", views.cliente_list),

]
