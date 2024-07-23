# Generated by Django 4.2.4 on 2024-03-18 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_order_store_alter_bankaccount_store"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="store",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.storemodel",
            ),
            preserve_default=False,
        ),
    ]