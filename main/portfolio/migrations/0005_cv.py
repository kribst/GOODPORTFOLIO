# Generated by Django 5.1.3 on 2024-11-06 03:02

import portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_work_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="CV",
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
                (
                    "file",
                    models.FileField(
                        upload_to="cv/",
                        validators=[portfolio.models.validate_single_cv],
                    ),
                ),
            ],
        ),
    ]