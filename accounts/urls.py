
from django.urls import path
from . import views as ac_views
urlpatterns =[
    path('signup/',ac_views.sign_up, name='signup'),
    path('match/',ac_views.email_match, name='match'),
    path('sendMail/',ac_views.sendMailOtp, name='sendMail'),
    path('verifyOtp/',ac_views.verifyOtp, name='verifyOtp'),
    path('register/',ac_views.register_view,name='register'),
    path('login/',ac_views.login_view,name='login'),
    path('logout/',ac_views.logout_view,name='logout_view'),
    path('',ac_views.dashbord,name='dashboard'),
    ]