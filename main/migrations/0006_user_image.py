# Generated by Django 4.2.1 on 2023-07-12 22:49

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.upload_users_image),
        ),
    ]