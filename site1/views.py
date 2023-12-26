from django.shortcuts import render
from .models import *
# Create your views here.
def db_table(request):
    return render(request, '1-db_table/index.html')

def db_table_add(request):
    return render(request, '1-db_table/add.html')

def db_table_update(request):
    return render(request, '1-db_table/update.html')

# Views for page 2 - Location folder
def location(request):
    locations=Location1.objects.all().using('server1')
    context={'locations':locations}
    return render(request, '2-location/index2.html',context)

def location_add(request):
    if request.method=='POST':
        location=Location1.objects.create(
            name=request.POST.get('name'),
            address=request.POST.get('address')
        )
        location.save(using='server1')
        return redirect('location')
    return render(request, '2-location/add2.html')

def location_update(request):
    return render(request, '2-location/update2.html')


# Views for 3-inventory folder
def inventory(request):
    inventories=Inventory1.objects.all().using('server1')
    context={'inventories':inventories}
    return render(request, '3-inventory/index3.html',context)

def inventory_add(request):
    return render(request, '3-inventory/add3.html')

def inventory_update(request):
    return render(request, '3-inventory/update3.html')

# Views for page 4 - Product folder
def product(request):
    products=Product1.objects.all().using('server1')
    context={'products':products}
    return render(request, '4-product/index4.html',context)

def product_add(request):
    return render(request, '4-product/add4.html')

def product_update(request):
    return render(request, '4-product/update4.html')

# Views for page 5 - ProductInventory folder
def product_inventory(request):
    return render(request, '5-product_inventory/index5.html')

def product_inventory_add(request):
    return render(request, '5-product_inventory/add5.html')

def product_inventory_update(request):
    return render(request, '5-product_inventory/update5.html')


def home(request):
    return render(request,'home/index.html')

def login(request):
    return render(request,'home/login.html')

def signup(request):
    return render(request,'home/signup.html')