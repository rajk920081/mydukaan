
from django.urls import path
from . import views as ac_views
urlpatterns =[
    path('signup/',ac_views.sign_up, name='signup'),
    path('match/',ac_views.email_match, name='match'),
    ]