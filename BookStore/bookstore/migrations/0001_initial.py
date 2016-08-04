# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('home_phone', models.CharField(max_length=13)),
                ('mobile_phone', models.CharField(max_length=13)),
                ('home_Add', models.CharField(max_length=150)),
                ('office_add', models.CharField(max_length=150)),
                ('slug', models.SlugField(default='No slug provided for address', help_text='Unique value for product url, created from name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('active', models.BooleanField(default=False)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('released_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('isbn', models.CharField(default='0000000000', max_length=15, primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to=b'')),
                ('about', models.TextField(default='No information provided for this book')),
                ('language', models.CharField(default='English', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(default='No slug provided for book', help_text='Unique value for product url, created from name')),
                ('meta_keywords', models.CharField(default='Meta_keyword for book', help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(default='meta_description for book', help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(default='meta-keyword for category', help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(default='meta-description for category', help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'Categories',
                'verbose_name': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('address', models.ManyToManyField(to='bookstore.Address')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='bookstore.Category'),
        ),
    ]
