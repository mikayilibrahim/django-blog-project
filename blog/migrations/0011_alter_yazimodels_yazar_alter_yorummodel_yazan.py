# Generated by Django 4.1.1 on 2022-09-24 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('blog', '0010_iletisimmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazimodels',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazilar', to='account.customusermodel'),
        ),
        migrations.AlterField(
            model_name='yorummodel',
            name='yazan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to='account.customusermodel'),
        ),
    ]
