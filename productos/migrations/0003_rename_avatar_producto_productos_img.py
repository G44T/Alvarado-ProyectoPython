# Generated by Django 5.1.5 on 2025-03-07 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='avatar',
            new_name='productos_img',
        ),
    ]
