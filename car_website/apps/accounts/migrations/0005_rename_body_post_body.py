# Generated by Django 4.1.3 on 2022-11-10 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='BODY',
            new_name='body',
        ),
    ]
