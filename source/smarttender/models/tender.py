from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новый'
    IN_PROGRESS = 'IN_PROGRESS', 'В процессе'
    DONE = 'DONE', 'Завершён'


class Tender(models.Model):
    lot = models.CharField(
        max_length=255,
        verbose_name='№ лота'
    )
    company = models.TextField(
        verbose_name='Учреждение'
    )
    name = models.TextField(
        verbose_name='Наименование'
    )
    additional_info = models.TextField(
        verbose_name='Дополнительная информация'
    )
    price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Цена за единицу'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
    )
    measure_unit = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Единица измерения'
    )
    planned_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Плановая сумма'
    )
    delivery_deadline = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Срок поставки'
    )
    proposed_product_name = models.TextField(
        null=True,
        blank=True,
        verbose_name='Наименование предлагаемого товара'
    )
    supplier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Поставщик'
    )
    price_without_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена без скидки'
    )
    supplier_discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Скидка от поставщика'
    )
    price_with_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена со скидкой'
    )
    vat = models.DecimalField(
        max_digits=5,
        decimal_places=2,
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
    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена закупа'
    )
    overall_info = models.TextField(
        verbose_name='Общая информация'
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    deadline = models.DateField(
        verbose_name='Крайний срок'
    )
    procurement_type = models.CharField(
        max_length=255,
        verbose_name='Вид закупа'
    )
    paper_ad_link = models.TextField(
        verbose_name='№/ссылка на бумажное объявление'
    )
    lot_link = models.TextField(
        verbose_name='Ссылка на электронный лот'
    )
    profit_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Коэффициент прибыли'
    )
    delivery_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Коэффициент доставки'
    )
    purchase_price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена закупа (за единицу)'
    )
    bidding_price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена подачи (за единицу)'
    )
    budget_price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена бюджета (за единицу)'
    )
    overall_profit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Общая прибыль с проекта'
    )
    overall_purchase_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Общая сумма закупа'
    )
    overall_contract_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Общая сумма договора'
    )
    winning_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Выигрышная цена'
    )
    commercial_offer_text = models.TextField(
        null=True,
        blank=True,
        verbose_name='Текст для КП'
    )
    status = models.CharField(
        max_length=30,
        choices=StatusChoice.choices,
        default=StatusChoice.NEW,
        verbose_name='Статус'
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
        return self.lot

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
