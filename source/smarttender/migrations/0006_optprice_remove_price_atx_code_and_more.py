# Generated by Django 4.2.1 on 2023-06-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttender', '0005_price_limit_price_opt_price_limit_price_per_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(blank=True, null=True, verbose_name='Торговое наименование')),
                ('mnn', models.CharField(blank=True, null=True, verbose_name='МНН')),
                ('medicine', models.CharField(blank=True, null=True, verbose_name='Лекарственная форма')),
                ('registration_number', models.CharField(blank=True, null=True, verbose_name='Регистрационное удостоверение')),
                ('limit_price_producer', models.CharField(blank=True, null=True, verbose_name='Предельная цена производителя')),
                ('limit_price_opt', models.CharField(blank=True, null=True, verbose_name='Предельная цена оптовой реализации')),
                ('limit_price_per', models.CharField(blank=True, null=True, verbose_name='Предельная цена розничной реализации')),
            ],
        ),
        migrations.RemoveField(
            model_name='price',
            name='atx_code',
        ),
        migrations.RemoveField(
            model_name='price',
            name='limit_price_opt',
        ),
        migrations.RemoveField(
            model_name='price',
            name='limit_price_per',
        ),
        migrations.RemoveField(
            model_name='price',
            name='limit_price_producer',
        ),
        migrations.RemoveField(
            model_name='price',
            name='number',
        ),
        migrations.RemoveField(
            model_name='price',
            name='producer',
        ),
    ]
