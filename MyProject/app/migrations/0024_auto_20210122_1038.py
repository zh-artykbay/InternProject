# Generated by Django 3.1.5 on 2021-01-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210122_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='technodom_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='monitor',
            name='technodom_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
