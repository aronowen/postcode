# Generated by Django 2.2.2 on 2019-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20191113_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='src_postcode',
            name='names',
            field=models.CharField(default=23, max_length=7),
            preserve_default=False,
        ),
    ]
