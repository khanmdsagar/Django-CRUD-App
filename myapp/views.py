from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Product
from django.contrib import messages
import re

# Create your views here.
# homepage
def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})


# saving data
def insertPage(request):
    return render(request, 'insert.html')

def saveData(request):
    if request.method == 'POST':
        if request.POST['name'] == '' or request.POST['price'] == '' or request.POST['quantity'] == '':
            messages.error(request, 'all fields required')
            return redirect('insert')
        else:
            new_product = Product(
                name = request.POST['name'].strip(),
                price = request.POST['price'].strip(),
                quantity = request.POST['quantity'].strip()
            )

            new_product.save()
            messages.success(request, "Saved")

            return redirect('insert')


# update data
def editPage(request, pid):
    product = Product.objects.get(id = pid)
    return render(request, 'edit.html', {'product': product})

def editData(request):
    if request.method == 'POST':
        if request.POST['name'] == '' or request.POST['price'] == '' or request.POST['quantity'] == '':
            messages.error(request, 'all fields required')
            return redirect('edit')
        else:
            pid = request.POST['id']
            product = Product.objects.filter(id = pid)

            product.update(
                name = request.POST['name'],
                price = request.POST['price'],
                quantity = request.POST['quantity']
            )

            messages.success(request, "Updated")

            return redirect('home')


# deleting data
def deletePage(request, id):
    return render(request, 'delete.html', {'id':id})

def deleteData(request):
    if request.method == 'POST':
        pid = request.POST['id']
        pro = Product.objects.get(id = pid)
        
        status = pro.delete()

        if status[0] == 1:
            messages.success(request, "Deleted")
        else:
            messages.success(request, "Delete failed")
            
        return redirect('home')

# search 
def searchPage(request):
    return render(request, 'search.html' )

def searchData(request):
    product = request.GET.get('name')
    if product:
        product = Product.objects.filter(name__icontains = product)
    else:
        product = Product.objects.all()
    return render(request, 'search.html', {'products': product} )
