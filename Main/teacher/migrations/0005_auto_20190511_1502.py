# Generated by Django 2.2 on 2019-05-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lg', '0004_auto_20190511_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ManyToManyField(to='lg.Teacher', verbose_name='班级对应教师'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birth',
            field=models.DateField(verbose_name='出生日期'),
        ),
    ]
