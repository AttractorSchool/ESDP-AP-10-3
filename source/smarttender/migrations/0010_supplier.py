# Generated by Django 4.2.1 on 2023-05-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarttender', '0009_remove_tenderapi_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(verbose_name='Наименование поставщика')),
                ('phone', models.CharField(verbose_name='Телефонный номер')),
                ('email', models.CharField(verbose_name='email')),
                ('product_name', models.TextField(verbose_name='Торговое наименование поставляемого товара')),
            ],
        ),
    ]