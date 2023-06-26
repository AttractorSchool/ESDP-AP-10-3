from django.db import models
from django.utils import timezone


# Пункт плана лота
class Plan(models.Model):
    subject_name_kz = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование заказчика на государственном языке'
    )
    subject_name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование заказчика на русском языке'
    )
    name_kz = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование на государственном языке'
    )
    name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование на русском языке'
    )
    count = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Количество / объем'
    )
    price = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Цена за единицу'
    )
    amount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая сумма, утвержденная для закупки'
    )
    ref_enstru_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Код КТРУ (ЕНС ТРУ)'
    )
    desc_kz = models.TextField(
        null=True,
        blank=True,
        verbose_name='Краткая характеристика на государственном языке'
    )
    desc_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Краткая характеристика на русском языке'
    )
    supply_date_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Срок поставки'
    )
    lot = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.Lot',
        on_delete=models.CASCADE,
        related_name='plans'
    )
    ref_units = models.ManyToManyField(
        blank=True,
        to='smarttender.RefUnit'
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
        return self.ref_units

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
