from django.urls import path
from . import views

urlpatterns = [
    # path("home", views.index, name="index"),
    # path("home/<int:id>", views.show, name="show"),
    
    path('drinks', views.drinks_all, name="all drinks"), #grabs all the drinks in the database
    path('drinks/<int:id>', views.drinks_id, name="individual drinks"), #grabs the drink by its id
    path('drinks/<str:alcohol_type>', views.drinks_category, name="drink category"), #grabs all the drinks that are under that category
         
    path('users', views.index_user, name="all users"),
    path('login', views.login, name="login"),
    path('create_user', views.create_user, name="create user"),
    path('user/<int:id>', views.show_user, name="individual user"),
    path('update_user/<int:id>', views.update_user, name="update user"),
    path('delete_users/<int:id>', views.delete_user, name="delete user"),
    # path('user', views.user_loggin), #possibly need this for secure login

    path('list', views.create_list, name="create list"), #create a list
    path('lists', views.index_lists, name="all lists"), #show all the lists for a particular user
    path('user_list/<int:id>', views.show_list, name="individual lists"), #shows an individual list from a particular user
    path('update_list/<int:id>', views.update_list, name="update lists"), #allows users to update a particular list
    path('delete_list/<int:id>', views.delete_list, name="delete lists"), #allow users to delete a list
         
    path('achievement/<int:id>', views.show_achievement, name="individual achievements"), #gets an achievement if a user has completed it
    path('update_achievement/<int:id>', views.update_achievement, name="update achievement"), #attaches an achievement to a user once they accomplish it
    
    path('user_analytic', views.create_analytic, name="create analytic"), #create an analytics for a particular user
    path('update_analytic/<int:id>', views.update_analytic, name="update analytic"), #updates a users analytics based on what they have liked and such
    
    
    path('create_comment', views.create_comment, name="create comments"), #creates a comment from a user for a drink
    path('user_comments/<int:id>', views.show_comments, name="user comments"), #shows individual comments from a user and needs to be attached to a drink
    path('update_comment/<int:id>', views.update_comment, name="update comments"), #allows users to edit a comment on a drink
    path('delete_comment/<int:id>', views.delete_comment, name="delete comment") #allows user to delete a comment
     
]