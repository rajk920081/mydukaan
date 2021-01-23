from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import MasterProduct
from .models import Cart
def count_cart(request):
    carts =Cart.objects.filter(user=request.user).count()
    return HttpResponse(carts)

def addToCart(request):
    status ="error"
    if request.is_ajax():
        proid =request.GET.get('proid')
        print(proid)
        product =MasterProduct.objects.get(pk=proid)
        print(request.user)
        qty1 =1
        cart =Cart.objects.create(product=product,user=request.user,qty=qty1)
        if cart:
            status=f"{product.name}, added successfully !"

    return HttpResponse(status)

def cartList(request):
    carts =Cart.objects.filter(user=request.user)
    return render(request,'carts/cart-list.html',{'carts':carts})