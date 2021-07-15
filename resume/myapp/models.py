from django.db import models


class uregi(models.Model):
   
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profile_image',blank=True)
    doc=models.FileField(upload_to='profile_document',blank=True)

