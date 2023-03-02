# Generated by Django 4.1.7 on 2023-02-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0002_slides'),
    ]

    operations = [
        migrations.AddField(
            model_name='slides',
            name='s1word3',
            field=models.CharField(default=1, max_length=30, verbose_name='третье слово слайда 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='s2word3',
            field=models.CharField(default=1, max_length=30, verbose_name='третье слово слайда 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='s3word3',
            field=models.CharField(default=1, max_length=30, verbose_name='третье слово слайда 3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slides',
            name='s1word2',
            field=models.CharField(max_length=30, verbose_name='второе слово слайда 1'),
        ),
        migrations.AlterField(
            model_name='slides',
            name='s2word2',
            field=models.CharField(max_length=30, verbose_name='второе слово слайда 2'),
        ),
        migrations.AlterField(
            model_name='slides',
            name='s3word2',
            field=models.CharField(max_length=30, verbose_name='второе слово слайда 3'),
        ),
    ]