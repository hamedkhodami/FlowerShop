from django.db import models
from django_jalali.db.models import jDateTimeField

class ContactUS(models.Model):
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=200, verbose_name="نام کامل")
    Phone = models.CharField(max_length=50, null=True, verbose_name="شماره تماس")
    ip = models.CharField(max_length=50, null=True, verbose_name="آیپی")
    Email = models.EmailField(max_length=200, verbose_name="ایمیل")
    Message = models.TextField(max_length=200, verbose_name="متن")
    created_at=jDateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


