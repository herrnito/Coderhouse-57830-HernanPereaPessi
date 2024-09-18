from django import forms
from .models import Cliente, Torta, Pedido
# from django.core.exceptions import ValidationError

# class ProductoCategoriaForm(forms.ModelForm):
#     class Meta:
#         model = ProductoCategoria
#         fields = '__all__'

#     def clean_nombre(self):
#         nombre = self.cleaned_data.get('nombre', '')

#         if not nombre.isalpha():
#             raise ValidationError("* El nombre solo puede contener letras. *")
        
#         if len(nombre) < 3 or len(nombre) >50:
#             raise ValidationError("* El nombre debe tener una longitud minima de 3 letras, o maxima 50. *")
        
#         return nombre

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class TortaForm(forms.ModelForm):
    class Meta:
        model = Torta
        fields = "__all__"

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
        