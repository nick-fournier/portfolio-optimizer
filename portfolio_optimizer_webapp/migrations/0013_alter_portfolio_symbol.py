# Generated by Django 4.2.16 on 2025-01-15 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_optimizer_webapp', '0012_expectedreturns_symbol_portfolio_symbol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='symbol',
            field=models.ForeignKey(db_column='symbol', on_delete=django.db.models.deletion.CASCADE, to='portfolio_optimizer_webapp.securitylist'),
        ),
    ]
