# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listed', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_matricule', models.IntegerField()),
                ('numero_ligne', models.IntegerField()),
                ('nombre_place', models.IntegerField()),
                ('id_ecran', models.TextField()),
                ('status_ecran', models.CharField(choices=[('O', 'opened'), ('F', 'closed')], max_length=1)),
                ('chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_gestion.Caracteristic')),
            ],
        ),
    ]
