# Generated by Django 3.0.5 on 2020-04-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
