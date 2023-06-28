# Generated by Django 4.2.1 on 2023-06-28 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smarttender", "0020_remove_lot_calculation_calculation_lot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calculation",
            name="lot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calculations",
                to="smarttender.lot",
            ),
        ),
    ]
