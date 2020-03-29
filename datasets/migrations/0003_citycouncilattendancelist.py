# Generated by Django 3.0 on 2020-03-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0002_auto_20200316_1905"),
    ]

    operations = [
        migrations.CreateModel(
            name="CityCouncilAttendanceList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crawled_at", models.DateTimeField()),
                ("crawled_from", models.URLField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("date", models.DateField()),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("council_member", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("presente", "Presente"),
                            ("falta_justificada", "Falta Justificada"),
                            ("licenca_justificada", "Licença Justificada"),
                            ("ausente", "Ausente"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]