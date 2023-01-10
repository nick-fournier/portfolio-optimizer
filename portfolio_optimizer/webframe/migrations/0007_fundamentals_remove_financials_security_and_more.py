# Generated by Django 4.1 on 2023-01-08 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webframe', '0006_delete_dividends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundamentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('net_income', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('net_income_common_stockholders', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('total_liab', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('total_assets', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('total_current_liabilities', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('total_current_assets', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('shares_outstanding', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('cash', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webframe.securitylist')),
            ],
        ),
        migrations.RemoveField(
            model_name='financials',
            name='security',
        ),
        migrations.DeleteModel(
            name='BalanceSheet',
        ),
        migrations.DeleteModel(
            name='Financials',
        ),
    ]
