# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20170218_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
