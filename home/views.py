from django.shortcuts import render

# Create your views here.
from products.models import MasterProduct

def homepage(request):
    products =MasterProduct.objects.filter()
    context ={'products':products}
    return render(request,'home/index.html',context)

def about_views(request):
    return render(request,'home/about.html')