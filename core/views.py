from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm

def listagem(request):
    pedido = Pedido.objects.all()

    context ={'pedido':pedido}

    return render(request, 'listagem.html', context )

def cadastrar(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appcore:listagem')
    return render(request, 'cadastrar.html', {'form': form})


def atualizar(request, pk):
    pedido = Pedido.objects.get(pk=pk)

    form = PedidoForm(request.POST or None,instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('appcore:listagem')
    return render(request, 'cadastrar.html', {'form': form})


def deletar(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.delete()
    return redirect('appcore:listagem')

    if request.method == 'Post':
        pedido.delete()
        return redirect('appcore:listagem')

    context ={'pedido': pedido}
    return  render(request, 'deletar.html', context)




