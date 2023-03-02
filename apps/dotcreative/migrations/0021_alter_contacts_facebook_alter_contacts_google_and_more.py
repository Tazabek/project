# Generated by Django 4.1.7 on 2023-02-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotcreative', '0020_contacts_facebook_contacts_google_contacts_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='facebook',
            field=models.CharField(max_length=155, verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='google',
            field=models.CharField(max_length=155, verbose_name='Ссылка на google'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='linkedin',
            field=models.CharField(max_length=155, verbose_name='Ссылка на linkedin'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='twitter',
            field=models.CharField(max_length=155, verbose_name='Ссылка на twitter'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='youtube',
            field=models.CharField(max_length=155, verbose_name='Ссылка на youtube'),
        ),
    ]