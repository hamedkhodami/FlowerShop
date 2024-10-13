from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView,name="صفحه  ورود"),
    path('register', views.register,name="صفحه  ورود"),
    path('loginUserInWeb', views.loginUserInWeb,name="چک کردن  ورود"),
    path('registerAction', views.registerAction,name="عملیات  ثبت نام"),
    path('CheckLogin', views.CheckLogin,name="چک کردن ورود"),
    path('LogOutUser', views.LogOutUser,name="خارج شدن"),
    path('ForgetPassword', views.ForgetPassword,name="ForgetPassword"),
]