from django.shortcuts import render,redirect
from .forms import ContactUsFrom
from .models import ContactUS
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url="/Users/")
def SaveAsk(request):
    if request.method=="POST":
        forms=ContactUsFrom(request.POST)
        if forms.is_valid():
            NewCommnet = ContactUS(Fullname=forms.cleaned_data["Fullname"], Phone=forms.cleaned_data["Phone"]
                                    , Email=forms.cleaned_data["Email"], Message=forms.cleaned_data["Message"])
            NewCommnet.save()
            forms = ContactUsFrom()
            return render(request=request,template_name="comments.html",context={"forms":forms, "success":" نظر شما با موفقیت ارسال شد و از طریق ایمیل و پیامک به شما در اسرع وقت پاسخ داده خواهد شد"} )
        else:
            return render(request=request,template_name="comments.html",context={"forms":forms, "error":"خطا در اعتبار سنجی فرم "} )

    else:
        forms = ContactUsFrom()
    return render(request=request,template_name="comments.html",context={"forms":forms})






