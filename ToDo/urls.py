from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_item),
    path('get/', get_items),
    path('get/<int:pk>/', get_one_item),
    path('update/<int:pk>/',update_item),
    path('delete/<int:pk>/',delete_item) 

]
