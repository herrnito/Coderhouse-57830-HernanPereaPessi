from django.shortcuts import render
from .models import Torta, Cliente


def torta_list(request):
    tortas= Torta.objects.all()
    contexto = {'tortas' : tortas}
    return render(request, 'pasteleria/torta_list.html', contexto)

def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes' : clientes}
    return render(request, 'pasteleria/cliente_list.html', contexto)




