# Generated by Django 4.2.7 on 2023-12-12 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menupage', '0003_lanchmenu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lanchmenu',
            old_name='Lanch_info',
            new_name='lanch_info',
        ),
        migrations.RenameField(
            model_name='lanchmenu',
            old_name='Lanch_name',
            new_name='lanch_name',
        ),
        migrations.RenameField(
            model_name='lanchmenu',
            old_name='Lanch_pic',
            new_name='lanch_pic',
        ),
        migrations.RenameField(
            model_name='lanchmenu',
            old_name='Lanch_price',
            new_name='lanch_price',
        ),
    ]