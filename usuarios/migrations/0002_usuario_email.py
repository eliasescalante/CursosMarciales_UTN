# Generated by Django 5.0.6 on 2024-10-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="email",
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
