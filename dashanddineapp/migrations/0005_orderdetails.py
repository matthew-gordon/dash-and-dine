# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashanddineapp', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashanddineapp.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='dashanddineapp.Order')),
            ],
        ),
    ]
