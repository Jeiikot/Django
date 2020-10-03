# Generated by Django 3.1.1 on 2020-10-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='certificate',
            field=models.CharField(choices=[('bachelor', 'Bachelor'), ('degree', 'University degree'), ('specialization', 'Specialization'), ('other', 'Other')], default='bachelor', max_length=25),
        ),
    ]
