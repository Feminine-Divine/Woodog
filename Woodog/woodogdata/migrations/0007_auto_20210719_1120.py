# Generated by Django 3.0.7 on 2021-07-19 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woodogdata', '0006_merge_20210719_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ['-created_date_time']},
        ),
    ]
