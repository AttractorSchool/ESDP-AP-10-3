from django.db import models
from django.utils import timezone


# Расчёты
class Calculation(models.Model):
    supplier_discount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Скидка от поставщика'
    )
    vat = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='НДС'
    )
    note = models.TextField(
        null=True,
        blank=True,
        verbose_name='Примечание'
    )
    manager = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Менеджер'
    )
    purchase_price = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Цена закупа'
    )
    overall_info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Общая информация'
    )
    paper_ad_link = models.TextField(
        null=True,
        blank=True,
        verbose_name='№/ссылка на бумажное объявление'
    )
    lot_link = models.TextField(
        null=True,
        blank=True,
        verbose_name='Ссылка на электронный лот'
    )
    profit_rate = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Коэффициент прибыли'
    )
    delivery_rate = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Коэффициент доставки'
    )
    purchase_price_per_unit = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Цена закупа (за единицу)'
    )
    bidding_price_per_unit = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Цена подачи (за единицу)'
    )
    budget_price_per_unit = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Цена бюджета (за единицу)'
    )
    overall_profit = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая прибыль с проекта'
    )
    overall_purchase_amount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая сумма закупа'
    )
    overall_contract_amount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Общая сумма договора'
    )
    winning_price = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Выигрышная цена'
    )
    commercial_offer_text = models.TextField(
        null=True,
        blank=True,
        verbose_name='Текст для КП'
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
        return self.trd_buy

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
