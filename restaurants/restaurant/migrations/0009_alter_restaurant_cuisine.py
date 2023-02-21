# Generated by Django 4.1.6 on 2023-02-21 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0002_alter_cuisine_name'),
        ('restaurant', '0008_alter_restaurant_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuisine.cuisine'),
        ),
    ]
