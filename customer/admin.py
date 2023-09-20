from django.contrib import admin
from .models import Customer, Dish, MealCategory

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'city', 'state')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = ('categories', 'name', 'price')

admin.site.register(MealCategory)