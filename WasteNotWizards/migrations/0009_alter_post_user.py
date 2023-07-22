# Generated by Django 4.2.3 on 2023-07-20 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WasteNotWizards', '0008_rename_address_user_city_user_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]