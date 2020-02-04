# Generated by Django 3.0.2 on 2020-02-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0038_auto_20200201_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='detalle',
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.ManyToManyField(blank=True, null=True, to='compras.Producto'),
        ),
    ]