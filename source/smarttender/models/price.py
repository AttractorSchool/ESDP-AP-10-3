from django.db import models

class Price(models.Model):
    trade_name = models.CharField(
        null=True,
        blank=True,
        verbose_name='Торговое наименование'
    )
    mnn = models.CharField(
        null=True,
        blank=True,
        verbose_name='МНН'
    )
    medicine = models.CharField(
        null=True,
        blank=True,
        verbose_name='Лекарственная форма'
    )
    registration_number = models.CharField(
        null=True,
        blank=True,
        verbose_name='Регистрационное удостоверение'
    )
    unit = models.CharField(
        null=True,
        blank=True,
        verbose_name='Единица измерения'
    )
    limit_price = models.CharField(
        null=True,
        blank=True,
        verbose_name='Предельная цена в рамках ГОБМП и ОСМС'
    )
    def __str__(self):
        return self.trade_name