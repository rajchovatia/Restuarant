# Generated by Django 4.2.7 on 2023-12-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_pic', models.ImageField(upload_to='')),
                ('about_name', models.CharField()),
                ('about_info', models.CharField()),
            ],
        ),
    ]
