# Generated by Django 5.0.6 on 2024-05-14 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('person_bringing_baby', models.CharField(max_length=100)),
                ('time_of_arrival', models.DateTimeField()),
                ('parents_names', models.CharField(max_length=200)),
                ('fee_in_ugx', models.DecimalField(decimal_places=2, max_digits=10)),
                ('period_of_stay', models.CharField(max_length=100)),
                ('baby_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price_per_item', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('education_level', models.CharField(blank=True, max_length=100, null=True)),
                ('contacts', models.CharField(blank=True, max_length=100, null=True)),
                ('on_duty', models.BooleanField(default=True)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DollSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar.baby')),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystar.sitter')),
            ],
        ),
    ]
