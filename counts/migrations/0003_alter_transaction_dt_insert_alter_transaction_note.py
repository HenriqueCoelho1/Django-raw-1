# Generated by Django 4.0 on 2021-12-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counts', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='dt_insert',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]