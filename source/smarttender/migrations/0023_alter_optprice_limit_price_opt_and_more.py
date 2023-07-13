# Generated by Django 4.2.1 on 2023-07-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smarttender", "0022_merge_20230704_1657"),
    ]

    operations = [
        migrations.AlterField(
            model_name="optprice",
            name="limit_price_opt",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Предельная цена оптовой реализации",
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="limit_price_per",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Предельная цена розничной реализации",
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="limit_price_producer",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Предельная цена производителя",
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="medicine",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Лекарственная форма",
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="mnn",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="МНН"
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="registration_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Регистрационное удостоверение",
            ),
        ),
        migrations.AlterField(
            model_name="optprice",
            name="trade_name",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Торговое наименование",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="limit_price",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Предельная цена в рамках ГОБМП и ОСМС",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="medicine",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Лекарственная форма",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="mnn",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="МНН"
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="registration_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Регистрационное удостоверение",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="trade_name",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Торговое наименование",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="unit",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Единица измерения"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="GMP",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="GMP"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="atx_classification",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ATX классификация"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="classification",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="dosage_and_concentration",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Дозировка и концентрация",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="generic",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Генерик"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="nd_number",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Номер НД"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="nd_type",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Тип НД"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="patent",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Патент"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="recipe",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Рецепт"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="register_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Регистрационный номер",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="shelf_life",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Срок хранения"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Тип"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="view",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Вид"
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="email",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="email"
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="phone",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Телефонный номер"
            ),
        ),
    ]
