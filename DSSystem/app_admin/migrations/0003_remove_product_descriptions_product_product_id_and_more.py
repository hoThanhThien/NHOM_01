# Generated by Django 5.0.7 on 2025-01-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descriptions',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='default_product_id', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
