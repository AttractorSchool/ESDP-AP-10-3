from django.db import models
from django.utils import timezone


class Product(models.Model):
    number = models.IntegerField(
        verbose_name='Номер',
        null=False,
        blank=False
    )
    register_number = models.CharField(
        verbose_name='Регистрационный номер',
        null=False,
        blank=False
    )
    type = models.CharField(
        verbose_name='Тип',
        null=False,
        blank=False
    )
    trade_name = models.TextField(
        verbose_name='Торговое наименование'
    )
    view = models.CharField(
        verbose_name='Вид'
    )
    register_date = models.DateField(
        null=True,
        blank=True
    )
    time = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Срок'
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата истечения'
    )
    producer = models.CharField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name='Производитель'
    )
    country = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Страна'
    )
    classification = models.CharField(
        null=True,
        blank=True
    )
    IGN = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='МНН'
    )
    atx_classification = models.CharField(
        null=True,
        blank=True,
        verbose_name='ATX классификация'
    )
    med_form = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Лек. форма'
    )
    release_form = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Форма выпуска'
    )
    shelf_life = models.CharField(
        verbose_name='Срок хранения'
    )
    GMP = models.CharField(
        verbose_name='GMP'
    )
    generic = models.CharField(
        verbose_name='Генерик'
    )
    recipe = models.CharField(
        verbose_name='Рецепт'
    )
    trademark = models.IntegerField(
        verbose_name='Торговая марка'
    )
    patent = models.CharField(
        verbose_name='Патент'
    )
    nd_type = models.CharField(
        null=True,
        blank=True,
        verbose_name='Тип НД'
    )
    nd_number = models.CharField(
        null=True,
        blank=True,
        verbose_name='Номер НД'
    )
    dosage_and_concentration = models.CharField(
        null=True,
        blank=True,
        verbose_name='Дозировка и концентрация'
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
        return self.number

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()