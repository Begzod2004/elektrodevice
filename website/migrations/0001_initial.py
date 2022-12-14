# Generated by Django 3.2.4 on 2022-02-15 17:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('info', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(blank=True, choices=[(True, 'Active'), (False, 'Inactive')], default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=170)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('info', ckeditor.fields.RichTextField()),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('tel', models.CharField(max_length=13)),
                ('tel2', models.CharField(max_length=13)),
                ('tel3', models.CharField(max_length=13)),
                ('mail', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('info', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(blank=True, choices=[(True, 'Active'), (False, 'Inactive')], default=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.servicetype')),
            ],
        ),
    ]
