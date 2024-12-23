# Generated by Django 4.2.4 on 2024-11-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0032_alter_noticemodel_user_alter_orderitem_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stocked",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("point_view", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stocked",
                        to="store.storemodel",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Stocked",
                "db_table": "stocked",
            },
        ),
        migrations.CreateModel(
            name="StockedImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.ImageField(upload_to="media/stocked/")),
                (
                    "stocked",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="store.stocked",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Stocked Images",
                "db_table": "stocked_images",
            },
        ),
    ]