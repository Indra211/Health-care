# Generated by Django 4.1.7 on 2023-04-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0003_new_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
