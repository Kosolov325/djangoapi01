# Generated by Django 4.0.3 on 2022-03-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_marca_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='desc',
            field=models.TextField(default='', verbose_name='Descrição'),
        ),
    ]
