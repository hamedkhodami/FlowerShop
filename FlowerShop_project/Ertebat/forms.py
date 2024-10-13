from django import forms
from .models import ContactUS


class ContactUsFrom(forms.Form):
    def __init__(self,*args, **kwargs):
        super(ContactUsFrom,self).__init__(*args, **kwargs)
        for item in ContactUsFrom.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"
    Fullname=forms.CharField(required=True,min_length=3,max_length=200,label=" نام کامل ")
    Phone=forms.IntegerField(required=True,label="شماره تماس")
    Email=forms.EmailField(required=True,label="ایمیل")
    Message=forms.CharField(widget=forms.Textarea,label="متن پیام",max_length=500)
