# Generated by Django 4.1.7 on 2023-02-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0030_remove_plan_name_plan_name1_plan_name2_plan_name3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='name1',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='name3',
        ),
    ]