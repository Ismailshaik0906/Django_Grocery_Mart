from django.urls import path
from .views import *
app_name='Cartapp'

urlpatterns = [
    path('viewcart/', viewcart, name='viewcart'),
    path('addtocart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('removefromcart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('search/',search_category,name='search'),
]