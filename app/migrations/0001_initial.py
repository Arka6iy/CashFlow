# Generated by Django 5.2a1 on 2025-05-17 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Kind",
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
                ("name", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Status",
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
                ("name", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Combo",
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.category"
                    ),
                ),
                (
                    "kind",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.kind"
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.subcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("created_at", models.DateTimeField()),
                ("amount", models.FloatField(blank=True, null=True)),
                ("note", models.TextField(blank=True, null=True)),
                (
                    "combo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.combo"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.status",
                    ),
                ),
            ],
        ),
    ]
