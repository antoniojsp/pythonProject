# Generated by Django 4.1.6 on 2023-02-06 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petiteurl', '0004_alter_urls_exp_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='urls',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
