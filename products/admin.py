from django.contrib import admin

# Register your models here.
from .models import MasterProCat,MasterProduct

admin.site.register(MasterProCat)
admin.site.register(MasterProduct)