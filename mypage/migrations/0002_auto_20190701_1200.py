# Generated by Django 2.2.2 on 2019-07-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdetails',
            name='cpic',
            field=models.ImageField(height_field=4000, max_length=10000, upload_to='', width_field=3000),
        ),
    ]
