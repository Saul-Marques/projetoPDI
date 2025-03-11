# Generated by Django 5.1.6 on 2025-03-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0013_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
