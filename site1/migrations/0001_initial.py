# Generated by Django 4.2.8 on 2023-12-26 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory1',
            fields=[
                ('inventory_id', models.IntegerField(primary_key=True, serialize=False)),
                ('modification_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Inventory1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location1',
            fields=[
                ('location_id', models.IntegerField(db_column='Location_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Location1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('describe', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Product1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productinventory1',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='site1.product1')),
            ],
            options={
                'db_table': 'ProductInventory1',
                'managed': False,
            },
        ),
    ]
