# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=500)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField()),
                ('frequency_unit', models.CharField(default=b'hour', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appointment', models.ForeignKey(to='remindr.Appointment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('dosage_amount', models.IntegerField(default=0)),
                ('dosage_unit', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReminderTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_to_take', models.DateTimeField(verbose_name=b'date to take medication')),
                ('appointment', models.ForeignKey(to='remindr.Appointment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('phone_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='medication',
            name='senior',
            field=models.ForeignKey(to='remindr.Senior', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dosage',
            name='medication',
            field=models.ForeignKey(to='remindr.Medication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='senior',
            field=models.ForeignKey(to='remindr.Senior', null=True),
            preserve_default=True,
        ),
    ]
