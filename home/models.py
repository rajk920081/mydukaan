from django.db import models

# Create your models here.


class MasterSlider(models.Model):
    POSTITION =(
        ("f",'face'),
        ('b','back')
         )

    title = models.CharField(max_length=100, blank=True, null=True)
    image= models.ImageField(upload_to="slider", default="slider.png")
    datetime = models.DateTimeField(auto_now=True)
    position =models.CharField(choices=POSTITION, max_length=10)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

