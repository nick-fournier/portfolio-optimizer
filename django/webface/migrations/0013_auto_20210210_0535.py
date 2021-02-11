# Generated by Django 3.1.4 on 2021-02-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webface', '0012_auto_20210209_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancesheet',
            name='capital_surplus',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='deferred_long_term_liab',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='minority_interest',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]