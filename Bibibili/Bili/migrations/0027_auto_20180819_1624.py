# Generated by Django 2.0.3 on 2018-08-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bili', '0026_auto_20180817_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='desc',
            field=models.TextField(help_text='内容', verbose_name='内容'),
        ),
    ]
