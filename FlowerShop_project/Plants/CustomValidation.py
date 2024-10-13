from django.core.exceptions import ValidationError
from .models import Houseplants

class Validation():

    def CheckEmpty(self,value):
        if value == "":
            raise ValidationError("قسمت مورد نظر نباید خالی باشد")

    def CheckAlpha(self,value):
        if not value.isalpha():
            raise ValidationError("مقدار وارد شده صحیح نیست ")

    def CheckNameExist(self,value):
        result=Houseplants.objects.filter(name=value).all()
        if len(result)>0:
            raise ValidationError("این مورد "+value+" ثبت شده است")