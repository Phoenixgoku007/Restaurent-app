# Generated by Django 4.1.6 on 2023-02-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='name',
            field=models.CharField(default='Italian', max_length=50),
        ),
    ]
