# Generated by Django 4.2 on 2023-04-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='produtos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='Nome_pedido',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]