# Generated by Django 4.1.7 on 2023-04-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0002_alter_appointment_id_alter_doctor_id_alter_report_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
