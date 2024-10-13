from django.db import models

# Create your models here.

class Houseplants(models.Model):
    name=models.CharField(max_length=100,verbose_name="نام گیاه")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="قیمت")
    description=models.TextField(verbose_name="توضیحات")
    image=models.ImageField(upload_to="files/images",verbose_name="تصویر")

    class Meta:
        verbose_name="گیاه"
        verbose_name_plural="گیاهان"
