# Generated by Django 4.1.7 on 2023-02-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0007_alter_categoryportfolio_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='categoryportfolio',
            name='foto',
            field=models.ImageField(null=True, upload_to='foto/', verbose_name='фото'),
        ),
        migrations.AddField(
            model_name='services',
            name='about',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='foto',
            field=models.ImageField(null=True, upload_to='service/', verbose_name='фото'),
        ),
        migrations.AddField(
            model_name='services',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='название услуги'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='number',
            field=models.IntegerField(default=1, unique=True, verbose_name='номер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(default=1, max_length=30, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
