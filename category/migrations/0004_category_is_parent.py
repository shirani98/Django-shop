# Generated by Django 4.0 on 2022-01-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_is_sub_category_sub_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_parent',
            field=models.BooleanField(default=True),
        ),
    ]
