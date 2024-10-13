from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactUS
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CommentView(request):
    return render(request=request,template_name="comment.html")

@login_required
def add_comment(request):
    if request.method=="POST":
        forms=ContactUS(request.POST)
        if forms.is_valid():
            comment= forms.save(commit=False)
            comment.user=request.user
            comment.save()
            return redirect("index.html")

    else:
        forms = ContactUS()
    return render(request=request,template_name="comment.html",context={"forms":forms})

