# Generated by Django 4.1.7 on 2023-02-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0031_rename_name1_plan_name_remove_plan_name2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название плана'),
        ),
    ]
