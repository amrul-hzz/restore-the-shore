# Generated by Django 4.1 on 2022-10-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0004_merge_20221031_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
    ]
