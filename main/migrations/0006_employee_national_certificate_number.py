# Generated by Django 3.1.2 on 2020-11-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201029_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='national_certificate_number',
            field=models.CharField(default='', max_length=25),
        ),
    ]
