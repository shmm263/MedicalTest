# Generated by Django 2.0.2 on 2018-02-15 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'managed': False, 'verbose_name': ('Пациент',), 'verbose_name_plural': 'Пациент'},
        ),
    ]
