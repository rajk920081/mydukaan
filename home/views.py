from django.shortcuts import render

# Create your views here.
from products.models import MasterProduct,MasterProCat
from .models import MasterSlider

def homepage(request):
    return render(request,'home/index.html')

def about_views(request):

    return render(request,'home/about.html')


from django.shortcuts import HttpResponse

def getSlider(request):
    sliders = MasterSlider.objects.filter(status=True)
    return render(request, 'home/slider.html', {'sliders': sliders,
                                                  })


def getProducts(request):
    products = MasterProduct.objects.filter().order_by('-pk')
    if request.is_ajax():
        mykey = request.GET.get('mykey')
        if mykey:
            print(mykey)
            products = MasterProduct.objects.filter(name__startswith=mykey).order_by('-pk')

    #         products = MasterProduct.objects.filter(name__startswith=vv)

    return render(request,'home/products.html',{'products':products,
                                                })

def getCategery(request):
    categery = MasterProCat.objects.filter().order_by('-pk')
    return render(request, 'home/categery.html', {'categery': categery,
                                                  })

def getMenu(request):
    categery = MasterProCat.objects.filter().order_by('-pk')
    return render(request, 'home/menu.html', {'categery': categery,
                                                  })


def product_details(request,link=None):
    # name =MasterProduct.objects.get() #ORM
    # onep = MasterProduct.objects.filter(price=500) | MasterProduct.objects.filter(price=250)
    #     # #filter() # querysert as list
    #     # #all() # querysert as list
    #     # #get() # one objects
    print(link)
    onep = MasterProduct.objects.get(slug=link)
    print(onep, type(onep))
    context ={
        'onep':onep
    }
    return render(request,'home/details.html',context)





