from django import forms
from .models import Cliente, Pedido, Endereco

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'



