# Generated by Django 4.1.3 on 2022-12-08 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0007_question_created_at_responce_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="responce",
            name="deck",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="cards.carddeck",
            ),
            preserve_default=False,
        ),
    ]
