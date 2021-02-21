# Generated by Django 3.1.7 on 2021-02-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webface', '0004_auto_20210214_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='financials',
            name='quarterly_price',
            field=models.DecimalField(decimal_places=2, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='financials',
            name='quarterly_variance',
            field=models.DecimalField(decimal_places=2, max_digits=17, null=True),
        ),
    ]
