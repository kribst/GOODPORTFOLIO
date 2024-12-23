# Generated by Django 5.1.2 on 2024-11-07 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_cv"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="work",
            name="description",
        ),
        migrations.RemoveField(
            model_name="work",
            name="problem",
        ),
        migrations.RemoveField(
            model_name="work",
            name="solution",
        ),
        migrations.CreateModel(
            name="WorkDescription",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="descriptions",
                        to="portfolio.work",
                    ),
                ),
            ],
        ),
    ]
