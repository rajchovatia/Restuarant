# Generated by Django 4.2.7 on 2023-12-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=255)),
                ('service_title', models.CharField(max_length=255)),
                ('service_dis', models.CharField(max_length=255)),
            ],
        ),
    ]