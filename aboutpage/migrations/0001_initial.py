# Generated by Django 4.2.7 on 2023-12-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_pic1', models.ImageField(upload_to='')),
                ('about_pic2', models.ImageField(upload_to='')),
                ('about_pic3', models.ImageField(upload_to='')),
                ('about_pic4', models.ImageField(upload_to='')),
            ],
        ),
    ]
