# Generated by Django 2.1.7 on 2019-05-15 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20190515_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='acc_type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='state',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='acc_type',
        ),
        migrations.DeleteModel(
            name='Account_type',
        ),
        migrations.DeleteModel(
            name='Stu_ate',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]