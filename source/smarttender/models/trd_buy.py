from django.db import models


class TrdBuy(models.Model):
    publish_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Дата"
    )
    end_date = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Крайний срок"
    )
    ref_trade_methods = models.ForeignKey(
        to="smarttender.RefTradeMethod",
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
