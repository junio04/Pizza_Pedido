from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, Cliente
from .forms import PedidoForm, ClienteForm

def listagem(request):
    pedido = Pedido.objects.all()

    context ={'pedido':pedido}

    return render(request, 'listagem.html', context )

def cadastrar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appcore:listagem')
    return render(request, 'cadastrar_pedido.html', {'form': form})


def atualizar(request, pk):
    pedido = Pedido.objects.get(pk=pk)

    form = PedidoForm(request.POST or None,instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('appcore:listagem')
    return render(request, 'cadastrar_pedido.html', {'form': form})


def deletar(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)

    if request.method == 'POST':
        pedido.delete()
        return redirect('appcore:listagem')

        context = {"pedido"}
    return render(request, 'deletar.html', context)


def cadastrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appcore:cadastrar_pedido')

    return render(request, 'cadastrar_cliente.html', {'form': form})

