from django import forms, views
from django.db.models.expressions import F
from django.shortcuts import render
from django.views import View
from.forms import uregi_forms
from .models import uregi

class homeview(View):
    def get(self,request):
        fm=uregi_forms()
        candates= uregi.objects.all()
        dic={
            'candates':candates,
            'form':fm,
        }
        return render(request,'myapp/home.html',dic)
       

    def post(self,request):
        fm=uregi_forms(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=uregi_forms()
        return render(request,'myapp/home.html',{'form':fm})

class Candate(View):
    def get(self,request , id):
        candidate=uregi.objects.get(pk=id)
        

        return render(request,'myapp/candateinformation.html',{'candidate':candidate})