# third-party
from model_utils.models import TimeStampedModel
# Django
from django.db import models
# local
from .managers import ProductManager

class Marca(TimeStampedModel):
    """
        Marca de un producto
    """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Provider(TimeStampedModel):
    """
        Proveedor de Producto
    """

    name = models.CharField(
        'Razon Social', 
        max_length=100
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'Telefonos',
        max_length=40,
        blank=True,
    )
    web = models.URLField(
        'Sitio web',
        blank=True,
    )


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    """
        Producto
    """

    UNIT_CHOICES = (
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    )

    barcode = models.CharField(
        max_length=13,
        unique=True
    )
    name = models.CharField(
        'Nombre', 
        max_length=40
    )
    provider = models.ForeignKey(
        Provider, 
        on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE
    )
    due_date = models.DateField(
        'Fecha de vencimiento',
        blank=True, 
        null=True
    )
    description = models.TextField(
        'Descripcion del Producto',
        blank=True,
    )
    unit = models.CharField(
        'Unidad de Medida',
        max_length=1,
        choices=UNIT_CHOICES, 
    )
    count = models.PositiveIntegerField(
        'Cantidad en Almacen',
        default=0
    )
    purchase_price = models.DecimalField(
        'Precio Compra',
        max_digits=7, 
        decimal_places=2
    )
    sale_price = models.DecimalField(
        'Precio Venta',
        max_digits=7, 
        decimal_places=2
    )
    num_sale = models.PositiveIntegerField(
        'Numero de Ventas',
        default=0
    )
    anulate = models.BooleanField(
        'Eliminado',
        default=False
    )

    #
    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name




