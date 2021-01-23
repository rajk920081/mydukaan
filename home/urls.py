
from django.urls import path
from . import views
from cart.views import count_cart,addToCart,cartList
urlpatterns =[
    path('',views.homepage, name='homepage'),
    path('about/',views.about_views, name='about'),
    path('getSlider/', views.getSlider, name='getSlider'),
    path('getProduct/', views.getProducts, name='getProducts'),
    path('getCategery/', views.getCategery, name='getCategery'),
    path('getMenu/', views.getMenu, name='getMenu'),
    path('cart-count/',count_cart, name='cart_count'),
    path('add-to-cart/',addToCart, name='addtocart'),
    path('cart-details/',cartList, name='cartList'),
    path('product_details/productid=<str:link>/', views.product_details, name='product_details'),

]