from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlantView,name="صفحه اصلی"),
    path('about', views.About,name="about"),
    path('StateUser', views.StateUser,name="StateUser"),

    #path('PlantView', views.PlantListView, name="لیست گیاهان"),

]