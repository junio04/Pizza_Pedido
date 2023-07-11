from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente
from .forms import ClienteForm
from .models import Pizza, Refrigerante


class CadastrarClienteView(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'cadastrar_cliente.html', {'form': form})

    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appcore:produtos')
        return render(request, 'cadastrar_cliente.html', {'form': form})



class SelecionarProdutosView(View):
    def get(self, request):
        pizzas = Pizza.objects.all()
        refrigerantes = Refrigerante.objects.all()
        context = {
            'pizzas': pizzas,
            'refrigerantes': refrigerantes,
        }
        return render(request, 'selecionar_produtos.html', context=context)

    def post(self, request):
        id_pizzas = request.POST.getlist('pizza')
        id_refrigerantes = request.POST.getlist('refrigerante')

        pizzas = Pizza.objects.filter(id__in=id_pizzas)
        refrigerantes = Refrigerante.objects.filter(id__in=id_refrigerantes)

        preco_total = sum(pizza.valor for pizza in pizzas) + sum(refrigerante.valor for refrigerante in refrigerantes)

        ultimo_cliente = Cliente.objects.last()

        context = {
            'pizzas': pizzas,
            'refrigerantes': refrigerantes,
            'ultimo_cliente': ultimo_cliente,
            'preco_total': preco_total,
        }

        return render(request, 'resumo_pedido.html', context=context)



class ConfirmarPedidoView(View):
    def get(self, request):
        return render(request, 'confirmar_pedido.html')

    def post(self, request):
        action = request.POST.get('action')

        if action == 'confirmar':
            # Lógica para confirmar a compra
            cliente = Cliente.objects.last()
            cliente.status = 'Compra Confirmada'
            cliente.save()
            return render(request, 'confirmacao_compra.html')

        elif action == 'cancelar':
            # Lógica para cancelar a compra
            return render(request, 'confirmacao_cancelamento.html')

        return redirect('appcore:produtos')