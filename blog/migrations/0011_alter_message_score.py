# Generated by Django 3.2 on 2021-06-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210630_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='score',
            field=models.TextField(),
        ),
    ]
