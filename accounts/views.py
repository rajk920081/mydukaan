from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def sign_up(request):
    return render(request,'accounts/signup.html',)

import json
import random
from django.contrib.auth.models import User
def email_match(request):
    if request.is_ajax():
        res = {'status': "success"}
        email1 =request.GET.get('ee')
        u =User.objects.filter(email=email1)
        if u:
            print(email1)
            res = {'status':"error"}

        return HttpResponse(json.dumps(res), content_type="application/json")
    return redirect('homepage')
from .utility.sendOtp import sendOtpMail
import random
def sendMailOtp(request):
    if request.is_ajax():
        res = {'status': "error"}
        email1 = request.GET.get('ee')
        if email1:
            otpv = random.randrange(1111,9999)
            res =sendOtpMail(request,email1)
            if res:
                print(otpv)
                request.session['myotp']=otpv
                print("mail send ")
                res = {'status': "success"}
                return HttpResponse(json.dumps(res), content_type="application/json")

    return HttpResponse("send mail")

def verifyOtp(request):
    verify ="failed"
    myotp =request.session.get('myotp')
    otp =request.GET.get('otp')
    if int(otp) ==int(myotp):
        verify="success"
    return HttpResponse(verify)


from django.contrib.auth.models import User
from .models import Userprofile

from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context =dict()
    if request.method=='POST':
        email =request.POST.get('email')
        password =request.POST.get('password')
        repassword =request.POST.get('repassword')
        if not password ==repassword:
            context['msg']="Password Not Match"
            return render(request, 'accounts/register.html', context)
        print(email,password)
        email_username =email.split("@")
        username1 =email_username[0]
        u =User.objects.create_user(username=username1,email=email,password=password)
        if u:
            Userprofile.objects.filter(user=u).update(password=password)
            print("User Register Successfully!")
            context['msg']="User Register Successfully!"
    return render(request,'accounts/register.html',context)

from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = dict()
    if request.method=='POST':
        username =request.POST.get('email')
        password =request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username, password=password)
        if user:
            print("data match")
            login(request,user)
            return redirect('dashboard')

        else:
            context['msg']="invalid email or Password"

    return render(request,'accounts/login.html',context)


def dashbord(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'accounts/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

