# Generated by Django 3.2.7 on 2021-10-05 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0003_auto_20211001_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='adress',
            new_name='addres',
        ),
    ]
