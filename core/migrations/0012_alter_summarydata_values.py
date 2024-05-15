# Generated by Django 5.0 on 2024-05-15 14:14

import clickhouse_backend.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_dataset_context_summarydata_metrics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarydata',
            name='values',
            field=clickhouse_backend.models.ArrayField(base_field=clickhouse_backend.models.Float64Field(), default=list),
        ),
    ]
