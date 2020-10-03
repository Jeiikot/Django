# Generated by Django 3.1.1 on 2020-10-02 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(help_text='Enter a Department name', max_length=150, validators=[django.core.validators.MinLengthValidator(2, 'The name must be more than 1 character')], verbose_name='department name'),
        ),
    ]