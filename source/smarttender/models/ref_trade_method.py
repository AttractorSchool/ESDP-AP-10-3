from django.db import models


class RefTradeMethod(models.Model):
    name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вид закупа"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
