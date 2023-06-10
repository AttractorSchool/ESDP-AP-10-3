from django.db import models


class Plan(models.Model):
    price = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Цена за единицу"
    )
    count = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Количество"
    )
    ref_units = models.ForeignKey(
        to="smarttender.RefUnit",
        on_delete=models.CASCADE,
    )
    amount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Плановая сумма"
    )
    supply_date_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name='Срок поставки'
    )
    ref_enstru_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Код ЕНС ТРУ"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
