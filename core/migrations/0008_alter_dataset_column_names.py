# Generated by Django 5.0 on 2024-05-15 11:33

import clickhouse_backend.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dataset_column_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='column_names',
            field=clickhouse_backend.models.ArrayField(base_field=clickhouse_backend.models.FixedStringField(max_bytes=256), default=[]),
        ),
    ]
