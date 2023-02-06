# Generated by Django 4.1.6 on 2023-02-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_value', models.CharField(blank=True, default='', max_length=8)),
                ('url', models.URLField(max_length=600)),
            ],
        ),
    ]