# Generated by Django 3.0.2 on 2020-01-31 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0028_auto_20200130_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='detalle',
        ),
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Factura'),
        ),
    ]