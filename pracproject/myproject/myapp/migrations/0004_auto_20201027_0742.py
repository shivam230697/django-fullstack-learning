# Generated by Django 3.1.2 on 2020-10-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customerentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerentry',
            name='tare_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
