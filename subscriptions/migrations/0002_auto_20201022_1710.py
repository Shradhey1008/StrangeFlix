# Generated by Django 3.1.2 on 2020-10-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='stripe_customer_id',
            field=models.CharField(max_length=40),
        ),
    ]