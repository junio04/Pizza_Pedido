from django.urls import path
from .views import listagem, cadastrar_pedido, cadastrar_cliente, atualizar,deletar, endereco

app_name = 'appcore'

urlpatterns =[
    path('', listagem, name = 'listagem'),
    path('cadastrar_pedido/', cadastrar_pedido, name = 'cadastrar_pedido' ),
    path('atualizar/<int:pk>/', atualizar, name = 'atualizar'),
    path('deletar/<int:pk>/', deletar, name= 'deletar'),
    path('cadastrar_cliente/', cadastrar_cliente, name = 'cadastrar_cliente'),
    path('endereco/', endereco, name = 'endereco' )

]