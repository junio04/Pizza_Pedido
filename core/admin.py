from django.contrib import admin

from .models import Endereco, Cliente, Pedido

admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Pedido)