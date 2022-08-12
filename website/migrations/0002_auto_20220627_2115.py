# Generated by Django 3.2 on 2022-06-27 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('agree_status', models.PositiveIntegerField(choices=[(1, 'Yuborilgan'), (2, 'Tasdiqlangan'), (3, 'Tugagan')], default=1)),
                ('hisob', models.BooleanField(choices=[(True, 'Hisob faktura yuborilmagan!'), (False, 'Hisob faktura yuborilgan***')], default=True)),
                ('status', models.BooleanField(choices=[(True, 'Faol'), (False, 'Faol emas')], default=False)),
            ],
            options={
                'verbose_name_plural': '1.Shartnomalar',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': '6.Turmanlar',
            },
        ),
        migrations.CreateModel(
            name='Meter_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': '4.Hisoblagich turi',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': '7.Viloyat',
            },
        ),
        migrations.CreateModel(
            name='Substation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.district')),
            ],
            options={
                'verbose_name_plural': '5.Nimstansiya',
            },
        ),
        migrations.CreateModel(
            name='Fider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('trant_tok', models.CharField(blank=True, max_length=100, null=True)),
                ('trant_n', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Faol'), (False, 'Faol emas')], default=False)),
                ('meter_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.meter_type')),
                ('substation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.substation')),
            ],
            options={
                'verbose_name_plural': '3.Fiderlar',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.region'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('inn', models.CharField(max_length=7, unique=True)),
                ('tel', models.CharField(blank=True, max_length=30, null=True)),
                ('login', models.CharField(blank=True, max_length=250, null=True)),
                ('passwrod', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Faol'), (False, 'Faol emas')], default=False)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.region')),
            ],
            options={
                'verbose_name_plural': '2.Mijozlar',
            },
        ),
        migrations.CreateModel(
            name='Conn_agre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.agreement')),
                ('fider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.fider')),
            ],
        ),
        migrations.AddField(
            model_name='agreement',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer'),
        ),
    ]