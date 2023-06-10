from django.db import models


class Supplier(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name='Поставщик'
    )
    phone = models.CharField(
        verbose_name='Телефонный номер',
        null=True,
        blank=True,
    )
    email = models.CharField(
        null=True,
        blank=True,
        verbose_name='email',
    )
    product_name = models.TextField(
        verbose_name='Торговое наименование поставляемого товара',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
