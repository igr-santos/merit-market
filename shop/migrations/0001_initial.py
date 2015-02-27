# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('qtty', models.PositiveIntegerField()),
                ('price_total', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=180, verbose_name='Name')),
                ('stok', models.PositiveIntegerField(verbose_name='Stok')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('picture', models.ImageField(upload_to=b'shop/', verbose_name='Picture')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='buylog',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buylog',
            name='purchased_for',
            field=models.ForeignKey(to='core.Customer'),
            preserve_default=True,
        ),
    ]
