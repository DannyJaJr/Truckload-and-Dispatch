# Generated by Django 3.2 on 2021-06-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_load_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
    ]