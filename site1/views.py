from django.shortcuts import render, redirect,get_object_or_404
from .models import *
# Create your views here.
def db_table(request):
    return render(request, '1-db_table/index.html')

def db_table_add(request):
    return render(request, '1-db_table/add.html')

def db_table_update(request,pk):
    product = Product1.objects.get(product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.quantity=request.POST.get("productQuantity")
        product.save()
        return redirect('product')
    context = {'product': product}
    return render(request, '1-db_table/update.html')

# Views for page 2 - Location folder
def location(request):
    locations=Location1.objects.all().using('server1')
    context={'locations':locations}
    return render(request, '2-location/index2.html',context)

def location_add(request):
    if request.method=='POST':
        location=Location1(
            name=request.POST.get('name'),
            address=request.POST.get('address')
        )
        location.save(using='server1')
        
        return redirect('location')
    return render(request, '2-location/add2.html')

def location_update(request,pk):
    location = get_object_or_404(Location1.objects.using('server1'),location_id=pk)

    if request.method=="POST":
        location.name = request.POST.get("productName")
        location.address = request.POST.get("productDescription")
        location.save()
        return redirect('location')
    context = {'location': location}

    return render(request, '2-location/update2.html',context)

def location_delete(request,pk):
    location=get_object_or_404(Location1.objects.using('server1'),location_id=pk)
    location.delete()
    return redirect('location')
    

# Views for 3-inventory folder
def inventory(request):
    locations=Location1.objects.all().using('server1')
    inventories=Inventory1.objects.all().using('server1')
    context={'inventories':inventories,}
    return render(request, '3-inventory/index3.html',context)

def inventory_add(request):
    if request.method=="POST":
        location=Location1.objects.using('server1').filter(name=request.POST.get('location'))
        print(location[0])
        inv=Inventory1(
            location=location[0]
        )
        inv.save(using='server1')
        return redirect('inventory')
    locations=Location1.objects.all().using('server1')
    context={'locations':locations}
    return render(request, '3-inventory/add3.html',context)

def inventory_update(request,pk):
    inventory = get_object_or_404(Inventory1.objects.using('server1'),inventory_id=pk)
    # productid
    # inventory. = request.POST.get("productName")
    return redirect('inventory')
    inventory.save()
    return render(request, '3-inventory/update3.html')

def inventory_delete(request,pk):
    inv=get_object_or_404(Inventory1.objects.using('server1'),inventory_id=pk)
    inv.delete()
    return redirect('inventory')

# Views for page 4 - Product folder
def product(request):
    products=Product1.objects.prefetch_related('productinventory1_set').using('server1')
    context={'products':products}
    return render(request, '4-product/index4.html',context)

def product_add(request):
    if request.method=='POST':
        product=Product1(
            product_name=request.POST.get('name'),
            describe=request.POST.get('description'),
            price=request.POST.get('price'),
            quantity=request.POST.get('stock'),
        )
        product.save(using='server1')
        inv=Inventory1.objects.using('server1').filter(location__name=request.POST.get('inventory'))
        prodinv=Productinventory1(product=product,inventory_id=inv[0])
        prodinv.save(using='server1')
        return redirect('product')
    inventories=Inventory1.objects.all().using('server1')
    context={'inventories':inventories}
    return render(request, '4-product/add4.html',context)

def product_inventory_add(request,pk):
    if request.method=="POST":
        product=get_object_or_404(Product1.objects.using('server1'),product_id=pk)
        inv=Inventory1.objects.using('server1').filter(location__name=request.POST.get('inventory'))
        prodinv=Productinventory1(product=product,inventory_id=inv[0])
        prodinv.save(using='server1')
    inventories=Inventory1.objects.all().using('server1')
    context={'inventories':inventories}
    return render(request,'4-product/add_inventory.html',context)

def product_update(request,pk):
    product = get_object_or_404(Product1.objects.using('server1'),product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.save(using='server1')
        return redirect('product')
    context = {'product': product}
    return render(request, '4-product/update4.html',context)

def product_delete(request,pk):
    product=get_object_or_404(Product1.objects.using('server1'),product_id=pk)
    product.delete()
    return redirect('product')

# # Views for page 5 - ProductInventory folder
# def product_inventory(request):
#     return render(request, '5-product_inventory/index5.html')

# deleted
# def product_inventory_update(request):

#     return render(request, '5-product_inventory/update5.html')


def home(request):
    return render(request,'home/index.html')

def login(request):
    return render(request,'home/login.html')

def signup(request):
    return render(request,'home/signup.html')