# Generated by Django 3.1.1 on 2020-10-02 22:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0002_auto_20201002_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Job position name', max_length=150, validators=[django.core.validators.MinLengthValidator(2, 'The name must be more than 1 character')], verbose_name='job position')),
                ('number_employees', models.IntegerField(blank=True, help_text='Enter a Number of Employees', verbose_name='Number of employees')),
                ('description', models.TextField(blank=True, help_text='Enter a Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
            ],
        ),
    ]
