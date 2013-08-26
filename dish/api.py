from tastypie.resources import ModelResource
from dish.models import Restaurant, Dish


class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        # resource_name = 'restaurant'

class DishResource(ModelResource):
	class Meta:
		queryset = Dish.objects.all()
		# resource_name = 'dish'