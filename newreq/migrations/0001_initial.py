# Generated by Django 3.1.4 on 2020-12-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('req_date', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('processed', models.BooleanField(default=False)),
                ('response', models.TextField(blank=True)),
            ],
        ),
    ]