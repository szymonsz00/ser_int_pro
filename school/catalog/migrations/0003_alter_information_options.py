# Generated by Django 3.2.9 on 2022-02-04 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220202_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'ordering': ['to_date'], 'permissions': (('can_change', 'Change'),)},
        ),
    ]
