from django.db import models

class OptPrice(models.Model):
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
    limit_price_producer = models.CharField(
        null=True,
        blank=True,
        verbose_name='Предельная цена производителя'
    )
    limit_price_opt = models.CharField(
        null=True,
        blank=True,
        verbose_name='Предельная цена оптовой реализации'
    )
    limit_price_per = models.CharField(
        null=True,
        blank=True,
        verbose_name='Предельная цена розничной реализации'
    )