# Generated by Django 4.1.1 on 2022-09-29 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_yazimodels_yazar_alter_yorummodel_yazan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='yaradilma_tarixi',
            new_name='yaradilma_tarix',
        ),
    ]
