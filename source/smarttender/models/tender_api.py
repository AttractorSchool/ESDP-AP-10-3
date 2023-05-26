from django.db import models


class TenderAPI(models.Model):
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
