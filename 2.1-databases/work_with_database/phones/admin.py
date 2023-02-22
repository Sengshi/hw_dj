from django.contrib import admin
from .models import Phone
# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'price',)


admin.site.register(Phone, PhoneAdmin)
