# Generated by Django 2.0.2 on 2018-03-03 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20180215_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lookuprajon',
            options={'managed': False, 'verbose_name': ('Районы',), 'verbose_name_plural': 'Районы'},
        ),
        migrations.AlterModelOptions(
            name='lookupregion',
            options={'managed': False, 'verbose_name': ('Регионы',), 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'managed': False, 'ordering': ['first_name'], 'verbose_name': ('Пациент',), 'verbose_name_plural': 'Пациент'},
        ),
    ]
