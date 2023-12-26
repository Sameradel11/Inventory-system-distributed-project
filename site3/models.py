from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Inventory3(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Location3', blank=True, null=True,on_delete=models.CASCADE)
    modification_date = models.DateField(blank=True, null=True,auto_now=True)

    class Meta:
        db_table = 'Inventory3'
    


class Location3(models.Model):
    location_id = models.AutoField(db_column='Location_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        db_table = 'Location3'
    
    def __str__(self):
        return self.name

class Product3(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)    
    describe = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)        
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Product3'
        
    def __str__(self):
        return self.product_name


class Productinventory3(models.Model):
    product = models.ForeignKey(Product3, on_delete=models.CASCADE)  # The composite primary key (product_id, id) found, that is not supported. The first column is selected.
    inventory_id = models.ForeignKey(Inventory3, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ProductInventory3'
        unique_together = (('product', 'inventory_id'),)

