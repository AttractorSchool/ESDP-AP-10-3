from django.db import models
from django.utils import timezone


# Код КТРУ (ЕНС ТРУ)
class EnsTruCode(models.Model):
    code = models.CharField(
        max_length=100,
        verbose_name='Код ЕНС ТРУ'
    )
    name = models.TextField(
        null=True,
        blank=True,
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
        return self.code

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
