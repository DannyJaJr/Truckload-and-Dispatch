# Generated by Django 3.2.5 on 2021-07-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_rename_to_phonenumber_my_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumber',
            old_name='my_phone',
            new_name='bid',
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='myphone',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
