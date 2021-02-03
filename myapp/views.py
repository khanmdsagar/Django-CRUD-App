from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})