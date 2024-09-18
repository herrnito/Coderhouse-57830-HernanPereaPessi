from django.shortcuts import render, redirect
from .models import Torta, Cliente, Pedido
from .forms import ClienteForm, TortaForm, PedidoForm

def index(request):
    return render(request, 'pasteleria/index.html')

def torta_list(request):
    query = request.GET.get("q")
    if query:
        tortas = Torta.objects.filter(nombre__icontains=query)
    else:
        tortas= Torta.objects.all()
    contexto = {'tortas' : tortas}
    return render(request, 'pasteleria/torta_list.html', contexto)

def cliente_list(request):
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(nombre__icontains=query)
    else:
        clientes = Cliente.objects.all()
    contexto = {'clientes' : clientes}
    return render(request, 'pasteleria/cliente_list.html', contexto)

def pedido_list(request):
    query = request.GET.get("q")
    if query:
        pedido = Pedido.objects.filter(nombre__icontains=query)
    else:
        pedidos = Pedido.objects.all()
    contexto = {'pedidos' : pedidos}
    return render(request, 'pasteleria/pedido_list.html', contexto)

def torta_create(request):
    if request.method == 'GET':
        form = TortaForm()
    if request.method == 'POST':
        form = TortaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('pasteleria:torta_list')   
    return render(request, 'pasteleria/torta_create.html', {"form" : form})

def pedido_create(request):
    if request.method == 'GET':
        form = PedidoForm()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('pasteleria:pedido_list')   
    return render(request, 'pasteleria/pedido_create.html', {"form" : form})


def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('pasteleria:cliente_list')   
    return render(request, 'pasteleria/cliente_create.html', {"form" : form})




