# Generated by Django 5.0.1 on 2024-02-05 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('casies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonMailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email подписчика')),
            ],
            options={
                'db_table': 'common_mailing_list',
            },
        ),
        migrations.CreateModel(
            name='CaseMailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email подписчика')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casies.case', verbose_name='Дело')),
            ],
            options={
                'db_table': 'case_mailing_list',
            },
        ),
    ]
