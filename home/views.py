from django.shortcuts import render

# Create your views here.
from products.models import MasterProduct,MasterProCat
from .models import MasterSlider

def homepage(request):
    sliders = MasterSlider.objects.filter(status=True)
    products = MasterProduct.objects.filter()
    procat = MasterProCat.objects.filter()
    context = {'products': products, 'sliders': sliders, 'procat': procat}
    return render(request,'home/index.html',context)

def about_views(request):
    return render(request,'home/about.html')


from django.shortcuts import HttpResponse

def getSlider(request):
    print('abcd helooo')
    if request.is_ajax():
        a =request.POST.get('nn1')
        b =request.POST.get('nn2')
        print(a,type(a), b , type(b))
        c =int(a)+int(b)
        return HttpResponse(c)
    return HttpResponse("no page found!")

counter =1
def getProducts(request):
    global counter
    products = MasterProduct.objects.filter()
    if request.is_ajax():
        vv = request.POST.get('vv')
        if vv:
            products = MasterProduct.objects.filter(name__startswith=vv)

    counter =counter +1

    return render(request,'home/products.html',{'products':products,
                                                'counter':counter
                                                })



