# Generated by Django 4.1.1 on 2022-09-21 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-id'], 'permissions': [('download_csv', 'Can download csv of all items')]},
        ),
    ]
