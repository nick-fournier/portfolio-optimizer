# Generated by Django 4.1 on 2023-03-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_optimizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitylist',
            name='has_fundamentals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='securitylist',
            name='has_prices',
            field=models.BooleanField(default=False),
        ),
    ]