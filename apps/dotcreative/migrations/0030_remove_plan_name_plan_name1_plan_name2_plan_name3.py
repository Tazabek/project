# Generated by Django 4.1.7 on 2023-02-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0029_includes_plan_remove_plan2_serv_remove_plan3_serv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='name',
        ),
        migrations.AddField(
            model_name='plan',
            name='name1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название плана 1'),
        ),
        migrations.AddField(
            model_name='plan',
            name='name2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название плана 2'),
        ),
        migrations.AddField(
            model_name='plan',
            name='name3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название плана 3'),
        ),
    ]
