# Generated by Django 3.0.5 on 2020-04-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
