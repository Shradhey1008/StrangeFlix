# Generated by Django 3.1.2 on 2020-10-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20201022_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='stripe_subscription_id',
            field=models.CharField(max_length=40),
        ),
    ]