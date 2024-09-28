# Generated by Django 5.1.1 on 2024-09-28 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("update", "0007_alter_event_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="image",
        ),
        migrations.AddField(
            model_name="eventimage",
            name="event",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="update.event",
            ),
        ),
    ]
