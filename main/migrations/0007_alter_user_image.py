# Generated by Django 4.2.1 on 2023-07-13 13:45

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='accounts/Blank-Profile-Picture.avif', upload_to=main.models.upload_users_image),
        ),
    ]
