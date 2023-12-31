# Generated by Django 4.2.3 on 2023-07-19 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WasteNotWizards', '0002_post_receiver_user_user_type_reservation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='Provider_type',
            new_name='provider_type',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='address',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='email',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_provider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_receiver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Receiver',
        ),
    ]
