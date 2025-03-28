# Generated by Django 5.0.4 on 2025-01-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_headerbackground'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeaderBackground',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Контактны', 'verbose_name_plural': 'Контактны'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Доставка и оплата', 'verbose_name_plural': 'Доставка и оплата'},
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='text_on_page',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='content',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='text_on_page',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='content',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='text_on_page',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='about',
            table=None,
        ),
        migrations.AlterModelTable(
            name='contactinfo',
            table=None,
        ),
        migrations.AlterModelTable(
            name='payment',
            table=None,
        ),
    ]
