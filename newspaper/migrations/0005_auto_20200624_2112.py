# Generated by Django 3.0.6 on 2020-06-24 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_auto_20200624_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='num_newspaper',
            new_name='newspaper_stable',
        ),
    ]
