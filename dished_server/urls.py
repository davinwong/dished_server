from django.conf.urls import patterns, include, url
from dish.api import RestaurantResource, DishResource, ReviewResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

dish_resource = DishResource()
restaurant_resource = RestaurantResource()
review_resource = ReviewResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dished_server.views.home', name='home'),
    # url(r'^dished_server/', include('dished_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(dish_resource.urls)),
    (r'^api/', include(restaurant_resource.urls)),
    (r'^api/', include(review_resource.urls)),
)
