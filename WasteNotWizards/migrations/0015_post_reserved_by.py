# Generated by Django 4.2.3 on 2023-07-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WasteNotWizards', '0014_post_reservation_status_post_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reserved_by',
            field=models.CharField(blank=True, null=True),
        ),
    ]
