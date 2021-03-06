# Generated by Django 3.2.4 on 2021-07-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(default='NOMBRE COMPLETO', max_length=100)),
                ('rut_cliente', models.CharField(default='RUT', max_length=11)),
                ('direccion', models.CharField(default='DIRECCION', max_length=100)),
                ('nro_boleta', models.CharField(default='NUMERO BOLETA', max_length=11)),
                ('fecha_compra', models.DateField(auto_now=True)),
                ('valor_neto', models.IntegerField()),
                ('valor_iva', models.IntegerField()),
                ('valor_total', models.IntegerField()),
            ],
            options={
                'db_table': 'venta',
            },
        ),
    ]
