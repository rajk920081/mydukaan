from django.shortcuts import render

# Create your views here.
from products.models import MasterProduct
from .models import MasterSlider

def homepage(request):
    sliders = MasterSlider.objects.filter(status=True)
    print(sliders)
    products =MasterProduct.objects.filter()
    context ={'products':products,'sliders':sliders}
    return render(request,'home/index.html',context)

def about_views(request):
    return render(request,'home/about.html')