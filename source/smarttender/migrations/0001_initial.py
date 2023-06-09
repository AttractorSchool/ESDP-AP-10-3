# Generated by Django 4.2.1 on 2023-05-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lot", models.CharField(max_length=255, verbose_name="№ лота")),
                ("company", models.TextField(verbose_name="Учреждение")),
                ("name", models.TextField(verbose_name="Наименование")),
                (
                    "additional_info",
                    models.TextField(verbose_name="Дополнительная информация"),
                ),
                (
                    "price_per_unit",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="Цена за единицу"
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "measure_unit",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Единица измерения",
                    ),
                ),
                (
                    "planned_amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="Плановая сумма"
                    ),
                ),
                (
                    "delivery_deadline",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Срок поставки",
                    ),
                ),
                (
                    "proposed_product_name",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Наименование предлагаемого товара",
                    ),
                ),
                (
                    "supplier",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Поставщик"
                    ),
                ),
                (
                    "supplier_discount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Скидка от поставщика",
                    ),
                ),
                (
                    "vat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="НДС",
                    ),
                ),
                (
                    "note",
                    models.TextField(blank=True, null=True, verbose_name="Примечание"),
                ),
                (
                    "manager",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Менеджер"
                    ),
                ),
                (
                    "purchase_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Цена закупа",
                    ),
                ),
                ("overall_info", models.TextField(verbose_name="Общая информация")),
                ("date", models.DateField(verbose_name="Дата")),
                ("deadline", models.DateField(verbose_name="Крайний срок")),
                (
                    "procurement_type",
                    models.CharField(max_length=255, verbose_name="Вид закупа"),
                ),
                (
                    "paper_ad_link",
                    models.TextField(verbose_name="№/ссылка на бумажное объявление"),
                ),
                (
                    "lot_link",
                    models.TextField(verbose_name="Ссылка на электронный лот"),
                ),
                (
                    "profit_rate",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Коэффициент прибыли",
                    ),
                ),
                (
                    "delivery_rate",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="Коэффициент доставки",
                    ),
                ),
                (
                    "purchase_price_per_unit",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Цена закупа (за единицу)",
                    ),
                ),
                (
                    "bidding_price_per_unit",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Цена подачи (за единицу)",
                    ),
                ),
                (
                    "budget_price_per_unit",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Цена бюджета (за единицу)",
                    ),
                ),
                (
                    "overall_profit",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Общая прибыль с проекта",
                    ),
                ),
                (
                    "overall_purchase_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Общая сумма закупа",
                    ),
                ),
                (
                    "overall_contract_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Общая сумма договора",
                    ),
                ),
                (
                    "winning_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="Выигрышная цена",
                    ),
                ),
                (
                    "commercial_offer_text",
                    models.TextField(
                        blank=True, null=True, verbose_name="Текст для КП"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "Новый"),
                            ("IN_PROGRESS", "В процессе"),
                            ("DONE", "Завершён"),
                        ],
                        default="NEW",
                        max_length=30,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удалён"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="Дата и время удаления"
                    ),
                ),
            ],
        ),
    ]
