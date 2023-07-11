# Generated by Django 4.2 on 2023-07-04 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(choices=[('pequena', 'Pequena'), ('media', 'Média'), ('grande', 'Grande')], max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='data_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='valor',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='preco_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='pizzas',
            field=models.ManyToManyField(to='core.pizza'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='refrigerantes',
            field=models.ManyToManyField(to='core.refrigerante'),
        ),
    ]