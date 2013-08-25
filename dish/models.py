from django.db import models

### DISH

MEAL = [
    'breakfast',
    'lunch',
    'dinner',
    'snack',
    'dessert',
    'brunch',
]

CATEGORY = [
    'main',
    'drink',
    'appetizer',
    'side',
    'dessert',
]

FOOD_GROUP = [
    'meat',
    'vegetable',
    'fruit',
    'seafood',
    'dairy',
    'grain',
]

# foods that people specifically seek out
FOOD_CLASS = [
    'burger',
    'hot_dog',
    'fries',
    'pizza',
    'taco',
    'fried_chicken',

    'sandwich',
    'salad',
    'soup',

    'pasta',
    'noodles',   
    'rice',
    'sushi',

    'steak',
    'ribs',
    'lobster',
    
    'ice_cream',

    'coffee',
    'juice',
    'wine',
    'beer',
]

DIETARY = [
    'vegetarian',
    'vegan',
    'gluten_free',
    'low_fat',
    'halal',
    'kocher',
    'nut_free'
]

### RESTAURANT

# starbucks? those ones in the middle of the mall like yogen fruz / timothy's
RESTAURANT_TYPE = [
    'fast_food',
    'casual_dining',
    'fine_dining',
    'cafe',
    'bar',
    'food_stand',
]

# many restaurant to many cuisines
CUISINE = [
    'korean',
    'korean_barbeque',
    'chinese',
    'japanese',
    'vietnamese',
    'indian',
    'teppanyaki',
    'monglian',

    'mexican',

    'italian',
    'french',
    'british',
    'egyptian',
]

# find all online
STATES = [
    'ON',
    'BC',
    'QC',
    'NY',
    'CA',
    'WA',
]

COUNTRIES = [
    'CA',
    'US',
]


class Restaurant(models.Model):
    """
    One restaurant to many addresses?
    delivery? take-out? drive-thru? reservations? wifi? parking? outdoor?
    kids? coffee? buffet? alcohol? smoking?
    TODO: fix address/postal code, phone number
    once you know postal code, are the other details (address, state) necessary?
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.Charfield(max_length=10)
    country = models.Charfield(max_length=30)
    postal_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    open_hour = models.TimeField(null=True, blank=True)
    close_hour = models.TimeField(null=True, blank=True)
    restaurant_type = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200, null=True, blank=True)


class Dish(models.Model):
    """
    could store some fields in review, but then calculate on every GET
    should have properties that are drawn from its reviews
    TODO: proper reference to array for selection field
    TODO: could have multiple food types?
    TODO: change image
    alcohol?
    """
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    food_group = models.CharField(max_length=200)
    dietary = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=200, null=True, blank=True)