# Generated by Django 2.0.3 on 2018-08-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bili', '0030_auto_20180821_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='member_level',
            field=models.CharField(choices=[('0', '普通用户'), ('1', '大会员'), ('2', '年费大会员')], help_text='会员等级', max_length=6, verbose_name='会员等级'),
        ),
    ]
