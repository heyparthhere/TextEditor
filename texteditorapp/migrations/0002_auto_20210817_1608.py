# Generated by Django 3.2.5 on 2021-08-17 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texteditorapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='last_name',
        ),
    ]
