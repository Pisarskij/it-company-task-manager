# Generated by Django 4.2 on 2023-08-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_worker_waiting_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="waiting_verified",
            field=models.BooleanField(default=True),
        ),
    ]
