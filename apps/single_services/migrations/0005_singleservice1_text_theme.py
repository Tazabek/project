# Generated by Django 4.1.7 on 2023-02-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_services', '0004_otherservs_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleservice1',
            name='text_theme',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='тема текста'),
        ),
    ]
