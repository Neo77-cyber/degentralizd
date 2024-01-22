# Generated by Django 5.0.1 on 2024-01-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='user_identifier',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_ash',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]