# Generated by Django 4.2.16 on 2024-11-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_optimizer_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='book_value',
            field=models.BigIntegerField(default=None, null=True),
        ),
    ]
