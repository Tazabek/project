# Generated by Django 4.1.7 on 2023-02-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_services', '0003_comments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherservs',
            name='slug',
            field=models.SlugField(default=1, max_length=30, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]