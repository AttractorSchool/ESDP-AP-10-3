from django.db import models


class Supplier(models.Model):
    name = models.IntegerField(
        verbose_name='Наименование поставщика',
        null=False,
        blank=False
    )
    phone = models.CharField(
        verbose_name='Телефонный номер',
        null=False,
        blank=False
    )
    email = models.CharField(
        verbose_name='email',
    )
    product_name = models.TextField(
        verbose_name='Торговое наименование поставляемого товара',
        null=False,
        blank=False
    )