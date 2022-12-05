# Generated by Django 4.1.3 on 2022-12-05 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_rename_cardgroup_carddeck"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("term", models.CharField(max_length=256)),
                ("definition", models.TextField(max_length=600)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.carddeck"
                    ),
                ),
            ],
        ),
    ]