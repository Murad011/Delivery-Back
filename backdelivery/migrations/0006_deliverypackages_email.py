# Generated by Django 3.1.2 on 2020-11-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backdelivery', '0005_delete_rfmscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverypackages',
            name='email',
            field=models.EmailField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
