# Generated by Django 5.0.1 on 2024-01-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('items', models.JSONField()),
                ('lat_long', models.CharField(max_length=255)),
                ('full_details', models.JSONField()),
            ],
        ),
    ]
