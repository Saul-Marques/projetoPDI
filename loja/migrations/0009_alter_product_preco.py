# Generated by Django 5.1.6 on 2025-02-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0008_remove_product_image_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
