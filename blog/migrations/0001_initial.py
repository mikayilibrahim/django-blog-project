# Generated by Django 4.1.1 on 2022-09-10 17:05

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KateqoriyaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='isim', unique=True)),
            ],
            options={
                'db_table': 'kateqoriya',
            },
        ),
    ]