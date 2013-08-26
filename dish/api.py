from tastypie.resources import ModelResource
from dish.models import Restaurant, Dish, Review


class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        # resource_name = 'restaurant'

class DishResource(ModelResource):
	class Meta:
		queryset = Dish.objects.all()
		# resource_name = 'dish'

class ReviewResource(ModelResource):
	class Meta:
		queryset = Review.objects.all()