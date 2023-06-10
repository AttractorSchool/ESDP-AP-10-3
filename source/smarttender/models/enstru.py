from django.db import models


class EnsTruCode(models.Model):
    code = models.CharField(
        max_length=100,
        verbose_name='Код ЕНС ТРУ'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
