# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bookname', models.CharField(max_length=200)),
                ('preface', models.CharField(max_length=4000)),
                ('AuthorName', models.CharField(max_length=200)),
                ('AvailableYN', models.CharField(default=b'Y', max_length=1)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
                ('uploadBook', models.FileField(upload_to=b'uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='genreType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReadHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
                ('bookid', models.ForeignKey(to='mybooks.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=4000)),
                ('password', models.CharField(max_length=200)),
                ('ActiveYN', models.CharField(default=b'Y', max_length=1)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('deletedYN', models.CharField(default=b'N', max_length=1)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 11, 9, 52, 103000))),
                ('bookid', models.ForeignKey(to='mybooks.Book')),
                ('userid', models.ForeignKey(to='mybooks.User')),
            ],
        ),
        migrations.AddField(
            model_name='readhistory',
            name='userid',
            field=models.ForeignKey(to='mybooks.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(to='mybooks.genreType'),
        ),
    ]
