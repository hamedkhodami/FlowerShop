from django.contrib import admin
from .models import Houseplants
from django.core.exceptions import ValidationError
from .CustomValidation import Validation
# Register your models here.

class HousePlanetAdmin(admin.ModelAdmin):
    list_display = ("name","price")

    def formfield_for_dbfield(self, db_field, **kwargs):
        validation=Validation()
        fromfild=super().formfield_for_dbfield(db_field,**kwargs)
        if db_field.name=="name":
            fromfild.validators.append(validation.CheckNameExist)
            fromfild.validators.append(validation.CheckAlpha)
        return fromfild


admin.site.register(Houseplants,HousePlanetAdmin)
