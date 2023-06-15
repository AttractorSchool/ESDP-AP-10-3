from django.db import models
from django.utils import timezone


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
        verbose_name='Путь до файла'
    )
    trd_buy = models.ForeignKey(
        to='smarttender.TrdBuy',
        on_delete=models.CASCADE,
        related_name='files'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время изменения'
    )
    is_deleted = models.BooleanField(
        null=False,
        default=False,
        verbose_name='Удалён'
    )
    deleted_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='Дата и время удаления'
    )

    def __str__(self):
        return self.name_ru

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
