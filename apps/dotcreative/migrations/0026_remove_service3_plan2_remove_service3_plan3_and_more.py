# Generated by Django 4.1.7 on 2023-02-16 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0025_service3_plan2_service3_plan3_service3_plan_1_plan1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service3',
            name='plan2',
        ),
        migrations.RemoveField(
            model_name='service3',
            name='plan3',
        ),
        migrations.RemoveField(
            model_name='service3',
            name='plan_1',
        ),
        migrations.AddField(
            model_name='plan1',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='Название плана'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Plan3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название плана')),
                ('curs', models.CharField(blank=True, max_length=10, null=True, verbose_name='Курс оплаты')),
                ('summ', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cymma oплаты оплаты')),
                ('cent', models.CharField(blank=True, max_length=2, null=True, verbose_name='cent')),
                ('include', models.CharField(blank=True, max_length=155, null=True, verbose_name='Что включает план')),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotcreative.service3', verbose_name='План')),
            ],
            options={
                'verbose_name_plural': 'План 3',
            },
        ),
        migrations.CreateModel(
            name='Plan2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название плана')),
                ('curs', models.CharField(blank=True, max_length=10, null=True, verbose_name='Курс оплаты')),
                ('summ', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cymma oплаты оплаты')),
                ('cent', models.CharField(blank=True, max_length=2, null=True, verbose_name='cent')),
                ('include', models.CharField(blank=True, max_length=155, null=True, verbose_name='Что включает план')),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotcreative.service3', verbose_name='План')),
            ],
            options={
                'verbose_name_plural': 'План 2',
            },
        ),
    ]
