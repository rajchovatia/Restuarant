# Generated by Django 4.2.7 on 2023-12-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutpage', '0003_aboutteam_about_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_pic1',
            field=models.ImageField(upload_to='about_pic'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic2',
            field=models.ImageField(upload_to='about_pic'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic3',
            field=models.ImageField(upload_to='about_pic'),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic4',
            field=models.ImageField(upload_to='about_pic'),
        ),
        migrations.AlterField(
            model_name='aboutteam',
            name='about_pic',
            field=models.ImageField(upload_to='team_pic'),
        ),
    ]
