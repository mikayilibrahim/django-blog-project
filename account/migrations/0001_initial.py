# Generated by Django 4.1.1 on 2022-09-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
            ],
            options={
                'verbose_name': 'İsdifadəçi',
                'verbose_name_plural': 'İsdifadəçilər',
                'db_table': 'user',
            },
        ),
    ]