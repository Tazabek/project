# Generated by Django 4.1.7 on 2023-02-16 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0028_alter_plan1_name_alter_plan2_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Includes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('include', models.CharField(blank=True, max_length=155, null=True, verbose_name='Что включает план')),
            ],
            options={
                'verbose_name_plural': 'Что включает',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название плана')),
                ('curs', models.CharField(blank=True, max_length=10, null=True, verbose_name='Курс оплаты')),
                ('summ', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cymma oплаты оплаты')),
                ('cent', models.CharField(blank=True, max_length=2, null=True, verbose_name='cent')),
            ],
            options={
                'verbose_name_plural': 'page Service3 План',
            },
        ),
        migrations.RemoveField(
            model_name='plan2',
            name='serv',
        ),
        migrations.RemoveField(
            model_name='plan3',
            name='serv',
        ),
        migrations.DeleteModel(
            name='Plan1',
        ),
        migrations.DeleteModel(
            name='Plan2',
        ),
        migrations.DeleteModel(
            name='Plan3',
        ),
        migrations.AddField(
            model_name='includes',
            name='plans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotcreative.plan', verbose_name='План'),
        ),
    ]