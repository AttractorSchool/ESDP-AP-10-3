from django.db import models


class TrdBuy(models.Model):
    ref_trade_methods = models.ForeignKey(
        to="smarttender.RefTradeMethod",
        on_delete=models.CASCADE
    )

    numberAnno = models.CharField(max_length=255, null=True, blank=True)
    nameKz = models.CharField(max_length=255, null=True, blank=True)
    nameRu = models.CharField(max_length=255, null=True, blank=True)
    totalSum = models.CharField(max_length=100, null=True, blank=True)
    countLots = models.IntegerField(null=True, blank=True)
    customerNameKz = models.TextField(null=True, blank=True)
    customerNameRu = models.TextField(null=True, blank=True)
    orgBin = models.CharField(max_length=255, null=True, blank=True)
    orgPid = models.CharField(max_length=255, null=True, blank=True)
    orgNameKz = models.CharField(max_length=255, null=True, blank=True)
    orgNameRu = models.CharField(max_length=255, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
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
    itogiDatePublic = models.DateField(null=True, blank=True)
    finYear = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения"
    )
