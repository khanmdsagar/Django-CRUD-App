from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Product
from django.contrib import messages

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})

def insertPage(request):
    return render(request, 'insert.html')

def saveData(request):
    if request.method == 'POST':
        if request.POST['name'] == '' or request.POST['price'] == '' or request.POST['quantity'] == '':
            messages.error(request, 'all fields required')
            return redirect('insert')
        else:
            new_product = Product(
                name = request.POST['name'],
                price = request.POST['price'],
                quantity = request.POST['quantity']
            )
            new_product.save()
            messages.success(request, 'Saved')
            return redirect('insert')