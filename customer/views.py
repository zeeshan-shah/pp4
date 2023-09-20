from django.shortcuts import render
from django.views import generic
from .models import Dish


def home(request):
    return render(request, 'customer/base.html')


def menu_view(request):
    # Retrieve all dishes from the Dish model
    dishes = Dish.objects.all()

    # Render the menu.html template with the dishes data
    return render(request, 'customer/menu.html', {'dishes': dishes})