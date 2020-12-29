from django.shortcuts import render

# Create your views here.
from products.models import MasterProduct,MasterProCat
from .models import MasterSlider

def homepage(request):
    sliders = MasterSlider.objects.filter(status=True)
    products = MasterProduct.objects.filter()
    procat = MasterProCat.objects.filter()
    context = {'products': products, 'sliders': sliders, 'procat': procat}
    return render(request,'home/index.html')

def about_views(request):
    return render(request,'home/about.html')


from django.shortcuts import HttpResponse
def getSlider(request):
    return HttpResponse("hello i m slider function")



