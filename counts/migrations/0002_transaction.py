# Generated by Django 4.0 on 2021-12-27 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_insert', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('note', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counts.category')),
            ],
        ),
    ]
