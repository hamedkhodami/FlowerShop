from django.contrib import admin
from .models import ContactUS
from .CustomValidation import Validation

# Register your models here.
class HouseErtebatAdmin(admin.ModelAdmin):
    list_display = ("Fullname", "Email", "created_at")

    def formfield_for_dbfield(self, db_field, **kwargs):
        validation=Validation()
        fromfild=super().formfield_for_dbfield(db_field,**kwargs)
        if db_field.name=="name":
            fromfild.validators.append(validation.CheckNameExist)
            fromfild.validators.append(validation.CheckAlpha)
        return fromfild

admin.site.register(ContactUS,HouseErtebatAdmin)

