# Generated by Django 4.2.1 on 2023-06-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smarttender", "0015_remove_trdbuy_ref_trade_methods_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="trdbuy", name="ref_subject_type",),
        migrations.AddField(
            model_name="trdbuy",
            name="ref_subject_type",
            field=models.ManyToManyField(blank=True, to="smarttender.refsubjecttype"),
        ),
    ]