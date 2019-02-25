# Generated by Django 2.0.13 on 2019-02-25 04:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('reg_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField()),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FruitSalesMgmt.Fruit')),
            ],
        ),
    ]