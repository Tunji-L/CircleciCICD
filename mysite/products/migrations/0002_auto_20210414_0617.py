# Generated by Django 3.2 on 2021-04-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='discription',
            new_name='description',
        ),
        migrations.AddField(
            model_name='products',
            name='features',
            field=models.BooleanField(default=True),
        ),
    ]
