# Generated by Django 3.2 on 2021-05-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='informe',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='realizada',
            field=models.BooleanField(default=False),
        ),
    ]