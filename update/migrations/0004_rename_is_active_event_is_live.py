# Generated by Django 5.1.1 on 2024-09-28 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("update", "0003_update_summary_updateimages"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="is_active",
            new_name="is_live",
        ),
    ]
