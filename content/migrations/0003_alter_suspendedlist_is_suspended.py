# Generated by Django 4.1 on 2022-09-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_suspendedlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suspendedlist",
            name="is_suspended",
            field=models.BooleanField(default=True),
        ),
    ]
