# Generated by Django 5.2.1 on 2025-05-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='data_fim',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='data_inicio',
        ),
    ]
