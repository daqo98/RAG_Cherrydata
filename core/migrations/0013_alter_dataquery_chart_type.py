# Generated by Django 5.0 on 2024-05-16 17:30

import clickhouse_backend.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_summarydata_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataquery',
            name='chart_type',
            field=clickhouse_backend.models.FixedStringField(default='pie', max_bytes=50),
        ),
    ]
