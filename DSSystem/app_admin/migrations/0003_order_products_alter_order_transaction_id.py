# Generated by Django 5.0.7 on 2025-02-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='app_admin.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True, unique=True),
        ),
    ]
