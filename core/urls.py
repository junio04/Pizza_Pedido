from django.urls import path
from .views import listagem, cadastrar, atualizar,deletar

app_name = 'appcore'

urlpatterns =[
    path('', listagem, name = 'listagem'),
    path('cadastrar/', cadastrar, name = 'cadastrar' ),
    path('atualizar/<int:pk>/', atualizar, name = 'atualizar'),
    path('deletar/<int:pk>/', deletar, name= 'deletar')

]