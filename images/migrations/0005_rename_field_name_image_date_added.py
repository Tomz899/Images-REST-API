# Generated by Django 4.0.4 on 2022-05-28 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='field_name',
            new_name='date_added',
        ),
    ]