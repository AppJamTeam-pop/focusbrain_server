# Generated by Django 5.1.4 on 2024-12-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focus',
            name='in_time',
            field=models.FloatField(),
        ),
    ]
