from django.db import models
from django.utils import timezone


# Лот объявления
class Lot(models.Model):
    lot_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Номер лота'
    )
    count = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общее количество'
    )
    amount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая сумма'
    )
    name_kz = models.TextField(
        null=True,
        blank=True,
        verbose_name='Наименование на государственном языке'
    )
    name_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Наименование на русском языке'
    )
    description_kz = models.TextField(
        null=True,
        blank=True,
        verbose_name='Детальное описание на государственном языке'
    )
    description_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Детальное описание на русском языке'
    )
    customer_name_kz = models.TextField(
        null=True,
        blank=True,
        verbose_name='Наименование заказчика на государственном языке'
    )
    customer_name_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Наименование заказчика на русском языке'
    )
    dumping = models.BooleanField(
        default=False,
        verbose_name='Признак демпинга'
    )
    trd_buy = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.TrdBuy',
        on_delete=models.CASCADE,
        related_name='lots'
    )
    products = models.ManyToManyField(
        blank=True,
        to='smarttender.Product'
    )
    suppliers = models.ManyToManyField(
        blank=True,
        to='smarttender.Supplier'
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
        return f'{self.lot_number} | {self.name_ru}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
