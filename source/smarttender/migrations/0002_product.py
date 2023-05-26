# Generated by Django 4.2.1 on 2023-05-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=255, verbose_name='Номер')),
                ('register_number', models.CharField(verbose_name='Регистрационный номер')),
                ('type', models.CharField(verbose_name='Тип')),
                ('trade_name', models.TextField(verbose_name='Торговое наименование')),
                ('view', models.CharField(verbose_name='Вид')),
                ('register_date', models.DateField()),
                ('time', models.DateField(blank=True, max_length=255, null=True, verbose_name='Срок')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дата истечения')),
                ('producer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('classification', models.CharField(blank=True, null=True)),
                ('IGN', models.CharField(blank=True, max_length=255, null=True, verbose_name='МНН')),
                ('atx_classification', models.CharField(blank=True, null=True, verbose_name='ATX классификация')),
                ('med_form', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лек. форма')),
                ('release_form', models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма выпуска')),
                ('shelf_life', models.CharField(verbose_name='Срок хранения')),
                ('GMP', models.IntegerField(verbose_name='GMP')),
                ('generic', models.IntegerField(verbose_name='Генерик')),
                ('recipe', models.IntegerField(verbose_name='Рецепт')),
                ('trademark', models.IntegerField(verbose_name='Торговая марка')),
                ('patent', models.IntegerField(verbose_name='Патент')),
                ('nd_type', models.IntegerField(blank=True, null=True, verbose_name='Тип НД')),
                ('nd_number', models.IntegerField(blank=True, null=True, verbose_name='Номер НД')),
                ('dosage_and_concentration', models.CharField(blank=True, null=True, verbose_name='Дозировка и концентрация')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалён')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления')),
            ],
        ),
    ]
