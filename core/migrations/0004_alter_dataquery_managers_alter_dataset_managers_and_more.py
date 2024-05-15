# Generated by Django 5.0 on 2024-05-15 09:16

import clickhouse_backend.models
import django.db.models.manager
import django.utils.timezone
import uuid
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_dataquery_chart_type'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='dataquery',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='dataset',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='dynamicchart',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='exporttable',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='insight',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='staticchart',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='summarydata',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='dataquery',
            name='activate_date',
        ),
        migrations.RemoveField(
            model_name='dataquery',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dataquery',
            name='deactivate_date',
        ),
        migrations.RemoveField(
            model_name='dataquery',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='dataquery',
            name='status',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='activate_date',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='created',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='deactivate_date',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='insight',
            name='status',
        ),
        migrations.AddField(
            model_name='dataquery',
            name='last_modification_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now=True),
        ),
        migrations.AddField(
            model_name='dataquery',
            name='upload_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='last_modification_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='upload_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insight',
            name='last_modification_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now=True),
        ),
        migrations.AddField(
            model_name='insight',
            name='upload_date',
            field=clickhouse_backend.models.DateTime64Field(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataquery',
            name='chart_type',
            field=clickhouse_backend.models.FixedStringField(default='pie', max_bytes=10),
        ),
        migrations.AlterField(
            model_name='dataquery',
            name='command_query',
            field=clickhouse_backend.models.StringField(),
        ),
        migrations.AlterField(
            model_name='dataquery',
            name='id',
            field=clickhouse_backend.models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataquery',
            name='request_status',
            field=clickhouse_backend.models.FixedStringField(choices=[('SUBMITTED', 'Submitted'), ('PROCESSING', 'Processing'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], max_bytes=10),
        ),
        migrations.AlterField(
            model_name='dataquery',
            name='user_prompt',
            field=clickhouse_backend.models.StringField(),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='clickhouse_db_name',
            field=clickhouse_backend.models.FixedStringField(max_bytes=200),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='clickhouse_table_name',
            field=clickhouse_backend.models.FixedStringField(max_bytes=200),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='id',
            field=clickhouse_backend.models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='path',
            field=clickhouse_backend.models.FixedStringField(max_bytes=256),
        ),
        migrations.AlterField(
            model_name='dynamicchart',
            name='chart_type',
            field=clickhouse_backend.models.FixedStringField(max_bytes=10),
        ),
        migrations.AlterField(
            model_name='dynamicchart',
            name='is_saved',
            field=clickhouse_backend.models.BoolField(),
        ),
        migrations.AlterField(
            model_name='dynamicchart',
            name='title_xaxis',
            field=clickhouse_backend.models.FixedStringField(max_bytes=50),
        ),
        migrations.AlterField(
            model_name='dynamicchart',
            name='title_yaxis',
            field=clickhouse_backend.models.FixedStringField(max_bytes=50),
        ),
        migrations.AlterField(
            model_name='exporttable',
            name='file_type',
            field=clickhouse_backend.models.FixedStringField(max_bytes=10),
        ),
        migrations.AlterField(
            model_name='exporttable',
            name='id',
            field=clickhouse_backend.models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exporttable',
            name='request_status',
            field=clickhouse_backend.models.FixedStringField(choices=[('SUBMITTED', 'Submitted'), ('PROCESSING', 'Processing'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], max_bytes=10),
        ),
        migrations.AlterField(
            model_name='exporttable',
            name='url',
            field=clickhouse_backend.models.StringField(),
        ),
        migrations.AlterField(
            model_name='insight',
            name='activate_context',
            field=clickhouse_backend.models.BoolField(),
        ),
        migrations.AlterField(
            model_name='insight',
            name='gpt_response',
            field=clickhouse_backend.models.StringField(),
        ),
        migrations.AlterField(
            model_name='insight',
            name='id',
            field=clickhouse_backend.models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='insight',
            name='request_status',
            field=clickhouse_backend.models.FixedStringField(choices=[('SUBMITTED', 'Submitted'), ('PROCESSING', 'Processing'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], max_bytes=10),
        ),
        migrations.AlterField(
            model_name='insight',
            name='user_prompt',
            field=clickhouse_backend.models.StringField(),
        ),
        migrations.AlterField(
            model_name='staticchart',
            name='title_xaxis',
            field=clickhouse_backend.models.FixedStringField(max_bytes=50),
        ),
        migrations.AlterField(
            model_name='staticchart',
            name='title_yaxis',
            field=clickhouse_backend.models.FixedStringField(max_bytes=50),
        ),
        migrations.AlterField(
            model_name='summarydata',
            name='id',
            field=clickhouse_backend.models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]