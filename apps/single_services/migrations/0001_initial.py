# Generated by Django 4.1.7 on 2023-02-21 19:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleService1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Single_service 1',
            },
        ),
        migrations.CreateModel(
            name='OtherServs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155, null=True, verbose_name='Название услуги')),
                ('experience', models.CharField(blank=True, max_length=155, null=True, verbose_name='Название сферы')),
                ('percent', models.CharField(blank=True, max_length=5, null=True, verbose_name='Проценты')),
                ('percent_giv', models.CharField(blank=True, max_length=2, null=True)),
                ('advantages', models.CharField(blank=True, max_length=155, null=True, verbose_name='Приимущества')),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='single_services.singleservice1', verbose_name='page')),
            ],
            options={
                'verbose_name_plural': 'График в тексте',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='имя')),
                ('proffession', models.CharField(max_length=155, verbose_name='должность')),
                ('text', models.TextField(verbose_name='текст')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='single_services.singleservice1')),
            ],
            options={
                'verbose_name_plural': 'Комменты',
            },
        ),
    ]