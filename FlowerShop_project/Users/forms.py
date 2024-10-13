from django import forms

class LoginUser(forms.Form):
    def __init__(self,*args, **kwargs):
        super(LoginUser,self).__init__(*args, **kwargs)
        for item in LoginUser.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    UserName=forms.CharField(required=True,label="نام کاربری")
    Password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)

class RegisterUser(forms.Form):
    def __init__(self,*args, **kwargs):
        super(RegisterUser,self).__init__(*args, **kwargs)
        for item in RegisterUser.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    Name=forms.CharField(required=True,label="نام ")
    Family=forms.CharField(required=True,label="نام خانوادگی ")
    Email=forms.EmailField(required=True,label="ایمیل")
    UserName=forms.CharField(required=True,label="نام کاربری")
    Password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)