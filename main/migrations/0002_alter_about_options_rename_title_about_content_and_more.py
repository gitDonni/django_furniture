# Generated by Django 5.0.4 on 2024-12-04 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'информацию о нас', 'verbose_name_plural': 'Информация о нас'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='title',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='text',
            new_name='text_on_page',
        ),
        migrations.RenameField(
            model_name='contactinfo',
            old_name='title',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='contactinfo',
            old_name='text',
            new_name='text_on_page',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='title',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='text',
            new_name='text_on_page',
        ),
    ]
