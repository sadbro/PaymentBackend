# Generated by Django 2.2.9 on 2023-03-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230316_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.UUIDField(),
        ),
    ]
