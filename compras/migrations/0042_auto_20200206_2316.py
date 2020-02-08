# Generated by Django 3.0.2 on 2020-02-07 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0041_auto_20200206_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='detalles',
        ),
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Factura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.ManyToManyField(blank=True, null=True, to='compras.Producto'),
        ),
    ]
