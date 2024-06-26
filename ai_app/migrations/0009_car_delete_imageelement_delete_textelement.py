# Generated by Django 4.0 on 2024-04-24 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_app', '0008_book_available_book_genre_book_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(blank=True, max_length=100)),
                ('rok', models.DateField(default=datetime.date.today)),
                ('automat', models.BooleanField(default=None)),
                ('cena', models.IntegerField(default=1000)),
                ('dostępność', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageElement',
        ),
        migrations.DeleteModel(
            name='TextElement',
        ),
    ]
