from django.db import models


class File(models.Model):
    file_path = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Документ лота"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
