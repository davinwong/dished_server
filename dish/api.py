from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from dish.models import Restaurant, Dish, Review

# TODO: better authentication

class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()
        authorization = Authorization()
        # resource_name = 'restaurant'


class DishResource(ModelResource):
	class Meta:
		queryset = Dish.objects.all()
		allowed_methods = ['get', 'post']
		authentication = BasicAuthentication()
		authorization = Authorization()
		# resource_name = 'dish'


# TODO: authorization: users can only edit their own reviews
class ReviewResource(ModelResource):
	class Meta:
		queryset = Review.objects.all()
		allowed_methods = ['get', 'delete', 'post', 'put']
		authentication = BasicAuthentication()
		authorization = Authorization()