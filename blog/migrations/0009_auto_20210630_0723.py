# Generated by Django 3.2 on 2021-06-30 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_smstext_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SmsText',
            new_name='Score',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='text',
            new_name='result',
        ),
    ]