# Generated by Django 3.2 on 2021-04-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0004_auto_20210421_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='texto',
            field=models.TextField(max_length=400, null=True),
        ),
    ]