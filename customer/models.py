from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class MealCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Zipcode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    street = models.ManyToManyField('Street', related_name='customers')
    city = models.ManyToManyField('City', related_name='customers')
    state = models.ManyToManyField('State', related_name='customers')
    zipcode = models.ManyToManyField('Zipcode', related_name='customers')

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    street = models.ForeignKey('Street', on_delete=models.CASCADE, related_name='customer_orders')
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='customer_orders')
    state = models.ForeignKey('State', on_delete=models.CASCADE, related_name='customer_orders')
    zipcode = models.ForeignKey('Zipcode', on_delete=models.CASCADE, related_name='customer_orders')
    items = models.ManyToManyField(Dish, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.name}"
