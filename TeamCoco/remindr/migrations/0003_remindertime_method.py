# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remindr', '0002_auto_20150201_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='remindertime',
            name='method',
            field=models.CharField(default=b'phone', max_length=5),
            preserve_default=True,
        ),
    ]
