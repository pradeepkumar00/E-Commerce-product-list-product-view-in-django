# Generated by Django 3.1.7 on 2021-04-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_remove_product_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inde',
            field=models.CharField(default=55, max_length=50),
            preserve_default=False,
        ),
    ]
