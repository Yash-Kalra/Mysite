# Generated by Django 2.2.2 on 2019-07-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0008_auto_20190705_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdetails',
            name='cpics',
            field=models.ImageField(upload_to=''),
        ),
    ]
