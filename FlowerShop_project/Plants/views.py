from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Houseplants
from .UserAuth import UserAuth
# Create your views here.



def PlantView(request):
    plants= Houseplants.objects.all()
    return render(request=request,template_name='index.html',context={'plants':plants})

def StateUser(request):
    user_st=UserAuth().StateLogin(request)
    if user_st["State"]:
        return render(request=request,template_name="StateUser.html",context={"user_st":user_st})
    else:
        return render(request=request,template_name="noneUser.html")

def About(request):
    return render(request=request,template_name="about.html")