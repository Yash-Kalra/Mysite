# Generated by Django 2.2.2 on 2019-07-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0009_auto_20190705_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdetails',
            name='cpics',
            field=models.ImageField(upload_to='images'),
        ),
    ]
