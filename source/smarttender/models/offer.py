from django.db import models


# Предложение лота (товар, поставщик, цена)
class Offer(models.Model):
    product = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.Product',
        on_delete=models.CASCADE
    )
    supplier = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.Supplier',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена товара'
    )
    lot = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.Lot',
        on_delete=models.CASCADE
    )
