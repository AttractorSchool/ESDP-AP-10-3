# Generated by Django 4.2.1 on 2023-06-13 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smarttender', '0002_enstrucode_file_product_reftrademethod_refunit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='IGN',
            new_name='ign',
        ),
    ]
