# Generated by Django 3.1.5 on 2021-01-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SulpakSmartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('current_price', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
