from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('accounts/login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('home/cooler/', views.cooler, name='cooler'),
    path('home/my_restaurants/', views.my_restaurants, name='my_restaurants'),
    path('discover/', views.discover, name='discover'),
    path('beers/<int:beer_id>/', views.beer_detail, name='beer_detail'),
    path('cooler/<int:beer_id>/add/<int:user_id>/', views.cooler_add, name='cooler_add'),
    path('cooler/<int:beer_id>/remove/<int:user_id>/', views.cooler_remove, name='cooler_remove'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/add/<int:user_id>/,', views.restaurant_add, name='restaurant_add'),
    path('restaurant/<int:restaurant_id>/remove/<int:user_id>/', views.restaurant_remove, name="restaurant_remove"),
    path('discover/search/', views.search, name='search'),
    path('beers/<int:beer_id>/tap/<int:restaurant_id>/', views.tap_to_rest, name="tap_to_rest"),
    path('beers/<int:beer_id>/untap/<int:restaurant_id>/', views.untap_from_rest, name="untap_from_rest"),
    path('beers/<int:beer_id>/add_photo/', views.add_photo, name='add_photo'),
]