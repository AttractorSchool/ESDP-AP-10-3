from django.db import models
from django.utils import timezone


# Вид предмета закупки
class RefSubjectType(models.Model):
    name_kz = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Предмет закупки на государственном языке'
    )
    name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Предмет закупки на русском языке'
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
