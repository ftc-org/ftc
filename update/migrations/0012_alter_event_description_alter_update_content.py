# Generated by Django 5.1.1 on 2024-09-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("update", "0011_rename_updateimages_updateimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="update",
            name="content",
            field=models.TextField(blank=True, default=""),
        ),
    ]
