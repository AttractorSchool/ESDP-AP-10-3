from django.db import models


class RefUnit(models.Model):
    name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Единица измерения"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
