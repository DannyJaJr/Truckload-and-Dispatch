# Generated by Django 3.2 on 2021-06-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_smstext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smstext',
            name='text',
            field=models.TextField(),
        ),
    ]
