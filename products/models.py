from django.db import models

# Create your models here.


class MasterProCat(models.Model):
    cat_id =models.AutoField(auto_created=True, primary_key=True, serialize=False)
    pic = models.ImageField(upload_to='pro_cot', default='cat.png')
    name =models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    update_time =models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

class MasterProduct(models.Model):
    pro_id =models.AutoField(auto_created=True, primary_key=True, serialize=False)
    cat_id =models.ForeignKey(MasterProCat, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product', default='pro.jpg')
    price =models.DecimalField(decimal_places=2, max_digits=10)
    discount_price =models.IntegerField(default=0)
    qty =models.IntegerField(default=0)
    desc = models.TextField(null = True, blank = True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)




from .extra_fun import unique_slug_generator
from django.db.models.signals import pre_save

def make_slug(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)


pre_save.connect(make_slug, sender=MasterProduct)

def make_slug_main(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)
pre_save.connect(make_slug_main, sender=MasterProCat)





