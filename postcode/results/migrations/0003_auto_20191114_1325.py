# Generated by Django 2.2.2 on 2019-11-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20191113_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='dentist',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='optician',
            field=models.BooleanField(default=False),
        ),
    ]
