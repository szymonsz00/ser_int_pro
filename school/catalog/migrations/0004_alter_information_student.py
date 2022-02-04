# Generated by Django 3.2.9 on 2022-02-04 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_information_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='student',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
