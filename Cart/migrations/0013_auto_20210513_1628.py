# Generated by Django 3.2 on 2021-05-13 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_alter_product_title'),
        ('Cart', '0012_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='completely_ordered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.product'),
        ),
    ]