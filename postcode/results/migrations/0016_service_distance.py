# Generated by Django 2.2.2 on 2019-11-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0015_remove_service_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='distance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
