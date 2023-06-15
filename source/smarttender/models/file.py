from django.db import models


class File(models.Model):
    original_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Оригинальное имя файла'
    )
    name_kz = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование документа на государственном языке'
    )
    name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование документа на русском языке'
    )
    file_path = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Путь до файла"
    )
    trd_buy = models.ForeignKey(
        to='smarttender.TrdBuy',
        on_delete=models.CASCADE,
        related_name='files'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
