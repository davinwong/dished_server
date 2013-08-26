# from django.db import models
# from django.contrib.auth.models import User
# from dish.models import Dish


# class Review(models.Model):
#     """
#     service? should be part of restaurant, but we review dishes
#     """
#     dish = models.ForeignKey(Dish)
#     user = models.ForeignKey(User)
#     created = models.DateTimeField(auto_now=True)
#     price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     size = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
#     overall = models.DecimalField(max_digits=4, decimal_places=3)
#     spice = models.DecimalField(max_digits=4, decimal_places=3)
#     sweet = models.DecimalField(max_digits=4, decimal_places=3)
#     salt = models.DecimalField(max_digits=4, decimal_places=3)
#     presentation = models.DecimalField(max_digits=4, decimal_places=3)
#     speed = models.IntegerField(help_text="minutes")
#     comment = models.CharField(max_length=200)