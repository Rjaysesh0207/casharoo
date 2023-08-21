# Generated by Django 4.2.4 on 2023-08-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0006_childtransaction_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[("debit", "Debit"), ("credit", "Credit")],
                default="debit",
                max_length=60,
            ),
            preserve_default=False,
        ),
    ]
