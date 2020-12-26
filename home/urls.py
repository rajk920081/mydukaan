
from django.urls import path
from . import views
urlpatterns =[
    path('',views.homepage, name='homepage'),
    path('about/',views.about_views, name='about'),
]