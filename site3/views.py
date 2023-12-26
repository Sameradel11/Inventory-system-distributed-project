from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
# Create your views here.
def db_table(request):
    return render(request, 'site3/1-db_table/index.html')

def db_table_add(request):
    return render(request, 'site3/1-db_table/add.html')

def db_table_update(request,pk):
    product = Product1.objects.get(product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.quantity=request.POST.get("productQuantity")
        product.save()
        return redirect('site3:product')
    context = {'product': product}
    return render(request, 'site3/1-db_table/update.html')

# Views for page 2 - Location folder
def location(request):
    locations=Location3.objects.all().using('server3')
    context={'locations':locations}
    return render(request, 'site3/2-location/index2.html',context)

def location_add(request):
    if request.method=='POST':
        location=Location3(
            name=request.POST.get('name'),
            address=request.POST.get('address')
        )
        location.save(using='server3')
        
        return redirect('site3:location')
    return render(request, 'site3/2-location/add2.html')

def location_update(request,pk):
    location = get_object_or_404(Location3.objects.using('server3'),location_id=pk)

    if request.method=="POST":
        location.name = request.POST.get("productName")
        location.address = request.POST.get("productDescription")
        location.save()
        return redirect('site3:location')
    context = {'location': location}

    return render(request, 'site3/2-location/update2.html',context)

def location_delete(request,pk):
    location=get_object_or_404(Location3.objects.using('server3'),location_id=pk)
    location.delete()
    return redirect('site3:location')
    

# Views for 3-inventory folder
def inventory(request):
    locations=Location3.objects.all().using('server3')
    inventories=Inventory3.objects.all().using('server3')
    context={'inventories':inventories,}
    return render(request, 'site3/3-inventory/index3.html',context)

def inventory_add(request):
    if request.method=="POST":
        location=Location3.objects.using('server3').filter(name=request.POST.get('location'))
        print(location[0])
        inv=Inventory3(
            location=location[0]
        )
        inv.save(using='server3')
        return redirect('site3:inventory')
    locations=Location3.objects.all().using('server3')
    context={'locations':locations}
    return render(request, 'site3/3-inventory/add3.html',context)

def inventory_update(request,pk):
    inventory = get_object_or_404(Inventory3.objects.using('server3'),inventory_id=pk)
    # productid
    # inventory. = request.POST.get("productName")
    return redirect('site3:inventory')
    inventory.save()
    return render(request, 'site3/3-inventory/update3.html')

def inventory_delete(request,pk):
    inv=get_object_or_404(Inventory3.objects.using('server3'),inventory_id=pk)
    inv.delete()
    return redirect('site3:inventory')

# Views for page 4 - Product folder
def product(request):
    products=Product3.objects.prefetch_related('productinventory3_set').using('server3')
    context={'products':products}
    return render(request, 'site3/4-product/index4.html',context)

def product_add(request):
    if request.method=='POST':
        product=Product3(
            product_name=request.POST.get('name'),
            describe=request.POST.get('description'),
            price=request.POST.get('price'),
            quantity=request.POST.get('stock'),
        )
        product.save(using='server3')
        inv=Inventory3.objects.using('server3').filter(location__name=request.POST.get('inventory'))
        print(inv)
        prodinv=Productinventory3(product=product,inventory_id=inv[0])
        prodinv.save(using='server3')
        return redirect('site3:product')
    inventories=Inventory3.objects.all().using('server3')
    context={'inventories':inventories}
    return render(request, 'site3/4-product/add4.html',context)

def product_inventory_add(request,pk):
    if request.method=="POST":
        product=get_object_or_404(Product3.objects.using('server3'),product_id=pk)
        inv=Inventory3.objects.using('server3').filter(location__name=request.POST.get('inventory'))
        prodinv=Productinventory3(product=product,inventory_id=inv[0])
        prodinv.save(using='server3')
        return redirect('site3:product')
    inventories=Inventory3.objects.all().using('server3')
    context={'inventories':inventories}
    return render(request,'site3/4-product/add_inventory.html',context)

def product_update(request,pk):
    product = get_object_or_404(Product3.objects.using('server3'),product_id=pk)
    if request.method == "POST":
        product.product_name = request.POST.get("productName")
        product.describe = request.POST.get("productDescription")
        product.price = request.POST.get("productPrice")
        product.quantity=request.POST.get("quantity")
        product.save(using='server3')
        return redirect('site3:product')
    context = {'product': product}
    return render(request, 'site3/4-product/update4.html',context)

def product_delete(request,pk):
    product=get_object_or_404(Product3.objects.using('server3'),product_id=pk)
    product.delete()
    return redirect('site3:product')

def home(request):
    return render(request,'site3/home/index.html')

def login(request):
    return render(request,'site3/home/login.html')

def signup(request):
    return render(request,'site3/home/signup.html')