# Generated by Django 3.0.5 on 2020-04-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(),
        ),
    ]
