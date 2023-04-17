from django import forms
from .models import Cliente, Endereco, Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'







