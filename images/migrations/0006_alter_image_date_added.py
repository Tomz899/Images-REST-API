# Generated by Django 4.0.4 on 2022-05-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_rename_field_name_image_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
