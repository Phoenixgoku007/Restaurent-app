# Generated by Django 4.1.6 on 2023-02-21 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0004_alter_cuisine_name'),
        ('restaurant', '0011_remove_restaurant_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cuisine.cuisine'),
        ),
    ]