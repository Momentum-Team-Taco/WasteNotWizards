# Generated by Django 4.2.3 on 2023-08-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WasteNotWizards', '0016_alter_reservation_lat_alter_reservation_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='foodlist',
            field=models.TextField(blank=True, null=True),
        ),
    ]
