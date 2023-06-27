from django.db import models
from django.utils import timezone


# Объявление
class TrdBuy(models.Model):
    number_anno = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Номер объявления'
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
    total_sum = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая сумма запланированная для закупки (Сумма закупки)'
    )
    count_lots = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Количество лотов в объявлении'
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
    org_bin = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='БИН Организатора'
    )
    org_pid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='ИД Организатора'
    )
    org_name_kz = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование организатора на государственном языке'
    )
    org_name_ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Наименование организатора на русском языке'
    )
    start_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Дата начала приема заявок'
    )
    publish_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Дата и время публикации'
    )
    end_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Дата окончания приема заявок"
    )
    itogi_date_public = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Дата публикации итогов'
    )
    fin_year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Финансовый год'
    )
    ref_trade_methods = models.ManyToManyField(
        blank=True,
        to='smarttender.RefTradeMethod'
    )
    ref_subject_type = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.RefSubjectType',
        on_delete=models.CASCADE,
        related_name='trd_buys'
    )
    ref_buy_status = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.RefBuyStatus',
        on_delete=models.CASCADE,
        related_name='trd_buys'
    )
    ref_type_trade = models.ForeignKey(
        null=True,
        blank=True,
        to='smarttender.RefTypeTrade',
        on_delete=models.CASCADE,
        related_name='trd_buys'
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
        return f'{self.number_anno} | {self.name_ru}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
