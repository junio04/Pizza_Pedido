from django.urls import path
from .views import CadastrarClienteView, SelecionarProdutosView, ConfirmarPedidoView

app_name = 'appcore'

urlpatterns = [
    path('cadastrar_cliente/', CadastrarClienteView.as_view(), name='cadastrar_cliente'),
    path('produtos/', SelecionarProdutosView.as_view(), name='produtos'),
    path('confirmar_pedido/', ConfirmarPedidoView.as_view(), name='confirmar_pedido'),

]

