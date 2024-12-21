# Generated by Django 5.1.4 on 2024-12-21 11:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0002_alter_focus_in_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='focus',
            unique_together={('user', 'date')},
        ),
        migrations.AlterModelTable(
            name='focus',
            table='focus',
        ),
    ]
