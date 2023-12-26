# Generated by Django 4.2.8 on 2023-12-26 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location2',
            fields=[
                ('location_id', models.AutoField(db_column='Location_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Location2',
            },
        ),
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('describe', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Product2',
            },
        ),
        migrations.CreateModel(
            name='Inventory2',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('modification_date', models.DateField(auto_now=True, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site2.location2')),
            ],
            options={
                'db_table': 'Inventory2',
            },
        ),
        migrations.CreateModel(
            name='Productinventory2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site2.inventory2')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site2.product2')),
            ],
            options={
                'db_table': 'ProductInventory2',
                'unique_together': {('product', 'inventory_id')},
            },
        ),
    ]
