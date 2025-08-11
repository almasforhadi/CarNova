from django.contrib import admin
from .models import BrandModel

# Register your models here.
# admin.site.register(BrandModel)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
                             'slug' : ('brand_name',)
                          }
    list_display = ['brand_name', 'slug']


admin.site.register(BrandModel,BrandAdmin) 
    