# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remindr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
