from django.db import models

CATEGORIES = [
    'main',
    'side',
    'drink',
    'dessert',
]

FOOD_TYPES = [
    'meat',
    'vegetable',
    'seafood',
]

class Dish(models.Model):
    """
    Could store some fields in review, but then calculate on every GET
    speed = minutes
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    restaurant = models.CharField(max_length=200)
    category = models.Charfield(max_length=200)
    food_type = models.Charfield(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=4, decimal_places=3)
    overall = models.DecimalField(max_digits=4, decimal_places=3)
    spice = models.DecimalField(max_digits=4, decimal_places=3)
    sweet = models.DecimalField(max_digits=4, decimal_places=3)
    salt = models.DecimalField(max_digits=4, decimal_places=3)
    presentation = models.DecimalField(max_digits=4, decimal_places=3)
    speed = models.IntegerField()