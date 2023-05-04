# Generated by Django 4.1.4 on 2023-05-04 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='matter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='expected_deliverydate',
            field=models.DateTimeField(default=datetime.date(2023, 5, 5)),
        ),
    ]