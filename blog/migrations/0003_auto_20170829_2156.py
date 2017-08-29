# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tmp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tmp',
        ),
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
