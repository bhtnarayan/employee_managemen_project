# Generated by Django 3.1.2 on 2020-10-29 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201028_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='home_phone_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
