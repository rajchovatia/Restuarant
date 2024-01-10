# Generated by Django 4.2.7 on 2023-12-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_pic', models.ImageField(upload_to='menu_picture')),
                ('menu_name', models.CharField(max_length=100)),
                ('menu_info', models.CharField(max_length=255)),
            ],
        ),
    ]