# Generated by Django 4.0.4 on 2022-04-29 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_sale', models.DateTimeField(verbose_name='Fecha de Venta')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad de Productos')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('type_invoce', models.CharField(choices=[('0', 'Boleta'), ('1', 'Factura'), ('2', 'Sin Comprobante')], max_length=2, verbose_name='TIPO')),
                ('type_payment', models.CharField(choices=[('0', 'Tarjeta'), ('1', 'Cash'), ('2', 'Bono'), ('3', 'Otro')], max_length=2, verbose_name='TIPO PAGO')),
                ('close', models.BooleanField(default=False, verbose_name='Venta Cerrada')),
                ('anulate', models.BooleanField(default=False, verbose_name='Venta Anulada')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_venta', to=settings.AUTH_USER_MODEL, verbose_name='cajero')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('price_purchase', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Precio Compra')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Venta')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Impuesto')),
                ('anulate', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sale', to='producto.product', verbose_name='producto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_sale', to='venta.sale', verbose_name='Codigo de Venta')),
            ],
            options={
                'verbose_name': 'Producto Vendido',
                'verbose_name_plural': 'Productos vendidos',
            },
        ),
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('barcode', models.CharField(max_length=13, unique=True)),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_car', to='producto.product', verbose_name='producto')),
            ],
            options={
                'verbose_name': 'Carrito de compras',
                'verbose_name_plural': 'Carrito de compras',
                'ordering': ['-created'],
            },
        ),
    ]
