# Generated by Django 3.0 on 2019-12-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='location',
            name='us_state',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
