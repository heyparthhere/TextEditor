# Generated by Django 3.2.5 on 2021-08-20 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texteditorapp', '0003_contactus_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='username',
        ),
    ]