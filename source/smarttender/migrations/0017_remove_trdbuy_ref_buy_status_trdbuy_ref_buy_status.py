# Generated by Django 4.2.1 on 2023-06-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smarttender", "0016_remove_trdbuy_ref_subject_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="trdbuy", name="ref_buy_status",),
        migrations.AddField(
            model_name="trdbuy",
            name="ref_buy_status",
            field=models.ManyToManyField(blank=True, to="smarttender.refbuystatus"),
        ),
    ]
