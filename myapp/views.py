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

            # if status[0] == 1:
            #     messages.success(request, "Saved")
            # else:
            #     messages.error(request, "Save failed")

            return redirect('insert')


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