# Generated by Django 2.2.9 on 2020-02-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsc', '0002_auto_20200201_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=52)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=16)),
                ('org_name', models.TextField()),
            ],
        ),
    ]
