from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def sign_up(request):
    return render(request,'accounts/signup.html',)

import json
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





