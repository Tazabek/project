# Generated by Django 4.1.7 on 2023-02-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherservs',
            old_name='serv',
            new_name='service',
        ),
        migrations.RemoveField(
            model_name='otherservs',
            name='percent_giv',
        ),
    ]