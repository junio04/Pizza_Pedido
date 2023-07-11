from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'endereco', 'cidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        nome = self.initial.get('nome', '')
        clientes = Cliente.objects.filter(nome=nome)

        if clientes.exists():
            cliente = clientes.first()
            self.fields['telefone'].initial = cliente.telefone
            self.fields['email'].initial = cliente.email
            self.fields['endereco'].initial = cliente.endereco
            self.fields['cidade'].initial = cliente.cidade



