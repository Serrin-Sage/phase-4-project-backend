from django.urls import path
from . import views

urlpatterns = [
    # path("home", views.index, name="index"),
    # path("home/<int:id>", views.show, name="show"),
    
    path('drinks', views.drinks_all), #grabs all the drinks in the database
    path('drinks/<int:id>', views.drinks_id), #grabs the drink by its id
    path('drinks/<str:alcohol_type>', views.drinks_category), #grabs all the drinks that are under that category
         
    path('user/', views.my_user),
    path('user/<int:id>', views.show_user),
    # path('user/<int:id>', views.update_user),
    # path('user/<int:id>', views.delete_user),
    # path('user', views.user_loggin), #possibly need this for secure login

    # path('list', views.list_create), #create a list
    # path('list/', views.list_all), #show all the lists for a particular user
    # path('list/<int:id>', views.list_show), #shows an individual list from a particular user
    # path('list/<int:id>', views.list_update), #allows users to update a particular list
    # path('list/<int:id>', views.list_delete), #allow users to delete a list
         
    # path('achievements/<int:id>', views.achievements_id), #gets an achievement if a user has completed it
    # path('achievements/<int:id>', views.achievements_update), #attaches an achievement to a user once they accomplish it
    
    # path('analysis', views.analysis_create), #create an analytics for a particular user
    # path('analysis/<int:id>', views.analysis.update), #updates a users analytics based on what they have liked and such
    
    # path('comments', views.comment_create), #creates a comment from a user for a drink
    # path('comments/<int:id>', views.comment_show), #shows individual comments from a user and needs to be attached to a drink
    # path('comments/<int:id>', views.comment_update), #allows users to edit a comment on a drink
    # path('comments/<int:id>', views.comment_delete) #allows user to delete a comment
    
]