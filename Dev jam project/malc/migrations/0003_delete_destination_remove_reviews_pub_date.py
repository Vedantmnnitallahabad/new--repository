# Generated by Django 4.1.6 on 2023-03-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malc', '0002_remove_destination_img_remove_destination_offer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='destination',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='pub_date',
        ),
    ]
