# Generated by Django 4.1.3 on 2022-12-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0003_town_alter_user_username_alter_farm_town'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]