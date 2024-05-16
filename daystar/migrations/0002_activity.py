# Generated by Django 5.0.6 on 2024-05-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_name', models.CharField(max_length=100)),
                ('payment_amount', models.FloatField()),
                ('baby_name', models.CharField(max_length=100)),
                ('baby_parent', models.CharField(max_length=100)),
            ],
        ),
    ]