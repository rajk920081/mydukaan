from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Userprofile(models.Model):
    userid =models.PositiveIntegerField(default=1000, auto_created=True,)
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    photo =models.ImageField(upload_to="accounts/uploads/images",default="pic.png")
    password =models.CharField(max_length=400)
    mobile =models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, created,instance,**kwargs):
    u=Userprofile.objects.last()
    if u:
        uid =int(u.userid) +1
    else:
        uid =1
    if created:
        Userprofile.objects.create(user=instance,userid=uid)

post_save.connect(create_profile,User)





