# Generated by Django 5.0.7 on 2025-01-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_product_active_user_active_user_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='app_admin.product'),
        ),
    ]
