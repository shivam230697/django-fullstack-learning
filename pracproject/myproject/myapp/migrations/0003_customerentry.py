# Generated by Django 3.1.2 on 2020-10-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_customerentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerEntry',
            fields=[
                ('rst_number', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('vehicle_number', models.CharField(max_length=10)),
                ('charges', models.IntegerField()),
                ('tare_weight', models.IntegerField()),
                ('gross_weight', models.IntegerField(blank=True, null=True)),
                ('net_weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
