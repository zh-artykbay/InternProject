# Generated by Django 3.1.5 on 2021-01-22 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_monitor_shopkz_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='shopkz_price',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='technodom_name',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='technodom_price',
        ),
    ]