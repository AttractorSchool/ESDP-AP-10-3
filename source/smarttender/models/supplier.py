from django.db import models
from django.utils import timezone


# Поставщик
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
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
