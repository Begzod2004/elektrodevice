# Generated by Django 3.2 on 2022-07-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20220725_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='mail',
            field=models.EmailField(max_length=50),
        ),
    ]