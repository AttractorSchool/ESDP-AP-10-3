from django.db import models


class Lot(models.Model):
    lot_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="№ лота"
    )
    customer_name_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name="Учреждение"
    )
    name_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name="Наименование"
    )
    description_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name="Дополнительная информация"
    )
    plans = models.ForeignKey(
        null=True,
        blank=True,
        to="smarttender.Plan",
        on_delete=models.CASCADE
    )
    trd_buy = models.ForeignKey(
        null=True,
        blank=True,
        to="smarttender.TrdBuy",
        on_delete=models.CASCADE
    )
    files = models.ForeignKey(
        null=True,
        blank=True,
        to="smarttender.File",
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        null=True,
        blank=True,
        to="smarttender.Product",
        on_delete=models.CASCADE
    )
    suppliers = models.ForeignKey(
        null=True,
        blank=True,
        to="smarttender.Supplier",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
