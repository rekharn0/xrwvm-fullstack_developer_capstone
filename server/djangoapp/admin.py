from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    

    list_display = ['car_make', 'name', 'type', 'year']
    list_filter = ['type', 'car_make', 'name', 'year',]
    search_fields = ['car_make', 'name']
    

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    
    
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [CarModelInline]

# Register models here


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
