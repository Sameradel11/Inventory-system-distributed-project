from django.shortcuts import render, redirect,get_object_or_404
from .models import *
# Create your views here.
def db_table(request):
    return render(request, 'site2/1-db_table/index.html')

def db_table_add(request):
    return render(request, 'site2/1-db_table/add.html')

def db_table_update(request,pk):
    product = Product1.objects.get(product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.quantity=request.POST.get("productQuantity")
        product.save()
        return redirect('site2:product')
    context = {'product': product}
    return render(request, 'site2/1-db_table/update.html')

# Views for page 2 - Location folder
def location(request):
    locations=Location2.objects.all().using('server2')
    context={'locations':locations}
    return render(request, 'site2/2-location/index2.html',context)

def location_add(request):
    if request.method=='POST':
        location=Location2(
            name=request.POST.get('name'),
            address=request.POST.get('address')
        )
        location.save(using='server2')
        
        return redirect('site2:location')
    return render(request, 'site2/2-location/add2.html')

def location_update(request,pk):
    location = get_object_or_404(Location2.objects.using('server2'),location_id=pk)

    if request.method=="POST":
        location.name = request.POST.get("productName")
        location.address = request.POST.get("productDescription")
        location.save()
        return redirect('site2:location')
    context = {'location': location}

    return render(request, 'site2/2-location/update2.html',context)

def location_delete(request,pk):
    location=get_object_or_404(Location2.objects.using('server2'),location_id=pk)
    location.delete()
    return redirect('site2:location')
    

# Views for 3-inventory folder
def inventory(request):
    locations=Location2.objects.all().using('server2')
    inventories=Inventory2.objects.all().using('server2')
    context={'inventories':inventories,}
    return render(request, 'site2/3-inventory/index3.html',context)

def inventory_add(request):
    if request.method=="POST":
        location=Location2.objects.using('server2').filter(name=request.POST.get('location'))
        print(location[0])
        inv=Inventory2(
            location=location[0]
        )
        inv.save(using='server2')
        return redirect('site2:inventory')
    locations=Location2.objects.all().using('server2')
    context={'locations':locations}
    return render(request, 'site2/3-inventory/add3.html',context)

def inventory_update(request,pk):
    inventory = get_object_or_404(Inventory2.objects.using('server2'),inventory_id=pk)
    # productid
    # inventory. = request.POST.get("productName")
    return redirect('site2:inventory')
    inventory.save()
    return render(request, 'site2/3-inventory/update3.html')

def inventory_delete(request,pk):
    inv=get_object_or_404(Inventory2.objects.using('server2'),inventory_id=pk)
    inv.delete()
    return redirect('site2:inventory')

# Views for page 4 - Product folder
def product(request):
    products=Product2.objects.prefetch_related('productinventory2_set').using('server2')
    context={'products':products}
    return render(request, 'site2/4-product/index4.html',context)

def product_add(request):
    if request.method=='POST':
        product=Product2(
            product_name=request.POST.get('name'),
            describe=request.POST.get('description'),
            price=request.POST.get('price'),
            quantity=request.POST.get('stock'),
        )
        product.save(using='server2')
        inv=Inventory2.objects.using('server2').filter(location__name=request.POST.get('inventory'))
        print(inv)
        prodinv=Productinventory2(product=product,inventory_id=inv[0])
        prodinv.save(using='server2')
        return redirect('site2:product')
    inventories=Inventory2.objects.all().using('server2')
    context={'inventories':inventories}
    return render(request, 'site2/4-product/add4.html',context)

def product_inventory_add(request,pk):
    if request.method=="POST":
        product=get_object_or_404(Product2.objects.using('server2'),product_id=pk)
        inv=Inventory2.objects.using('server2').filter(location__name=request.POST.get('inventory'))
        prodinv=Productinventory2(product=product,inventory_id=inv[0])
        prodinv.save(using='server2')
        return redirect('site2:product')
    inventories=Inventory2.objects.all().using('server2')
    context={'inventories':inventories}
    return render(request,'site2/4-product/add_inventory.html',context)

def product_update(request,pk):
    product = get_object_or_404(Product2.objects.using('server2'),product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.quantity=request.POST.get("quantity")
        product.save(using='server2')
        return redirect('site2:product')
    context = {'product': product}
    return render(request, 'site2/4-product/update4.html',context)

def product_delete(request,pk):
    product=get_object_or_404(Product2.objects.using('server2'),product_id=pk)
    product.delete()
    return redirect('site2:product')

def home(request):
    return render(request,'site2/home/index.html')

def login(request):
    return render(request,'site2/home/login.html')

def signup(request):
    return render(request,'site2/home/signup.html')