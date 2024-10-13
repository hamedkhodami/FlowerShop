from django.contrib import admin
from .models import Cart,CartItrm
# Register your models here.

class CartsAdmin(admin.ModelAdmin):
    list_display = ("user","created_at")

admin.site.register(Cart,CartsAdmin)