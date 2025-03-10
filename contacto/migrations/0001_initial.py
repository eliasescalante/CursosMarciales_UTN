# Generated by Django 5.0.6 on 2024-10-29 19:53

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Consulta",
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
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                ("descripcion", models.TextField()),
                ("mail", models.EmailField(blank=True, max_length=50, null=True)),
                (
                    "estado_respuesta",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Contestada", "Contestada"),
                            ("No Contestada", "No Contestada"),
                            ("En_Proceso", "En Proceso"),
                        ],
                        default="No Contestada",
                        max_length=15,
                    ),
                ),
                ("telefono", models.CharField(blank=True, max_length=90, null=True)),
                ("fecha", models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name="Respuesta",
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
                ("respuesta", models.TextField()),
                (
                    "fecha",
                    models.DateField(
                        blank=True, default=datetime.datetime.now, editable=False
                    ),
                ),
                (
                    "consulta",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacto.consulta",
                    ),
                ),
            ],
        ),
    ]
