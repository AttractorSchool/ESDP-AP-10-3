# Generated by Django 4.2.1 on 2023-06-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttender', '0004_price_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='limit_price_opt',
            field=models.CharField(blank=True, null=True, verbose_name='Предельная цена оптовой реализации'),
        ),
        migrations.AddField(
            model_name='price',
            name='limit_price_per',
            field=models.CharField(blank=True, null=True, verbose_name='Предельная цена розничной реализации'),
        ),
        migrations.AddField(
            model_name='price',
            name='limit_price_producer',
            field=models.CharField(blank=True, null=True, verbose_name='Предельная цена производителя'),
        ),
        migrations.AddField(
            model_name='price',
            name='producer',
            field=models.CharField(blank=True, null=True, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='price',
            name='limit_price',
            field=models.CharField(blank=True, null=True, verbose_name='Предельная цена в рамках ГОБМП и ОСМС'),
        ),
        migrations.AlterField(
            model_name='price',
            name='number',
            field=models.CharField(blank=True, null=True, verbose_name='Номер'),
        ),
    ]