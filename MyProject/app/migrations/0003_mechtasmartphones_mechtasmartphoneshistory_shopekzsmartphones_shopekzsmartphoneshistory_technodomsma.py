# Generated by Django 3.1.5 on 2021-01-11 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sulpaksmartphoneshistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MechtaSmartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('current_price', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShopeKzSmartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('current_price', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TechnodomSmartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('current_price', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TechnodomSmartphonesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=200)),
                ('time', models.TimeField(auto_now_add=True)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sulpaksmartphones')),
            ],
        ),
        migrations.CreateModel(
            name='ShopeKzSmartphonesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=200)),
                ('time', models.TimeField(auto_now_add=True)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sulpaksmartphones')),
            ],
        ),
        migrations.CreateModel(
            name='MechtaSmartphonesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=200)),
                ('time', models.TimeField(auto_now_add=True)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sulpaksmartphones')),
            ],
        ),
    ]
