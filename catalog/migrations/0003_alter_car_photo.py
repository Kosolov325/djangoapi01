# Generated by Django 4.0.3 on 2022-03-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_car_photo_alter_car_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(default='https://cdn.motor1.com/images/mgl/2gwok/s3/mercedes-benz-e-300-exclusive.jpg', upload_to='static/assets', verbose_name='foto'),
        ),
    ]
