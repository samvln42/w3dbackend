# Generated by Django 4.2.4 on 2024-11-14 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0034_goodsmodel_stocked_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="goodsmodel",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="goodsmodel",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]