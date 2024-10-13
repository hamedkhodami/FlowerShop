from django.db import models
from django.contrib.auth.models import User
from Plants.models import Houseplants
from django_jalali.db.models import jDateTimeField
# Create your models here.


class Cart(models.Model):
    user =models.OneToOneField (User,on_delete=models.CASCADE,verbose_name="کاربر")
    created_at=jDateTimeField(auto_now_add=True,verbose_name="اضافه شده در تاریخ")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"


class CartItrm(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name="سبد خرید")
    plant=models.ForeignKey(Houseplants,on_delete=models.CASCADE,verbose_name="گیاه")
    quantity=models.PositiveIntegerField(default=1,verbose_name="تعداد")
    added_at=jDateTimeField(auto_now_add=True,verbose_name="اضافه شده در تاریخ")

    def __str__(self):
        return f"{self.quantity} x {self.plant.name}"