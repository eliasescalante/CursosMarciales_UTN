# Generated by Django 5.0.6 on 2024-11-24 23:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("academia", "0003_noticia_mostrar_alter_noticia_titulo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clase",
            name="sede",
        ),
        migrations.RemoveField(
            model_name="inscripcionclase",
            name="clase",
        ),
        migrations.RemoveField(
            model_name="inscripcionclase",
            name="usuario",
        ),
        migrations.DeleteModel(
            name="Sede",
        ),
        migrations.DeleteModel(
            name="Clase",
        ),
        migrations.DeleteModel(
            name="InscripcionClase",
        ),
    ]
