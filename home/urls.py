from django.urls import path
from . import views

urlpatterns = [
    # path("home", views.index, name="index"),
    # path("home/<int:id>", views.show, name="show"),
    #need a drink path for all drinks, drinks/category, and drinks/id
    path('drinks', views.drinks_all), #grabs all the drinks in the database
    path('drinks/<int:id>', views.drinks_id), #grabs the drink by its id
    path('drinks/<str:alcohol_type>', views.drinks_category), #grabs all the drinks that are under that category


         
]