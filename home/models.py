from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    username = models.CharField(max_length=64, blank=False, unique=True, null=False)
    email = models.EmailField(blank=False, unique=True, null=False)
    password = models.CharField(max_length=64, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=64, blank=False, null=False)
    logged_in = models.BooleanField(default=True)
    #comment belongs to a user


    def __str__(self):
        return f"{self.first_name} is my first name {self.last_name} is my last name, username= {self.username}, password= {self.password}, is {self.age} years old, and I live in {self.location}"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'age': self.age,
            'location': self.location,
            'logged_in': self.logged_in
        }
class Drink(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    # this is the category which will be conencted to the front end (get Drink.alcohol_type === beer)
    alcohol_type = models.CharField(max_length=64, blank=False, null=False)
    # example is white wine, pilsner, like sub_category
    sub_alc_type = models.CharField(max_length=64, blank=False, null=False)
    distiller = models.CharField(max_length=100, blank=False, null=False)
    dist_location = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000)
    abv = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=200)
    # user_lists = models.ForeignKey(UserLists, on_delete=models.CASCADE)

    def __str__(self):
        return f"THIS IS {self.name} and it is {self.alcohol_type} and it was made by {self.distiller} in {self.dist_location}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'alcohol_type': self.alcohol_type,
            'sub_alc_type': self.sub_alc_type,
            'distiller': self.distiller,
            'dist_location': self.dist_location,
            'description': self.description,
            'abv': self.abv,
            'image': self.image
            # 'user_lists': self.user_lists
        }
class UserLists(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drinks = models.ManyToManyField(Drink)
    # array = starts blank and post to the list with drinks selected by user

    def __str__(self):
        return f"This be my {self.name} list"
    
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'user': self.user,
            'drinks': self.drinks
        }
class Analytics(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(User)
    userlist = models.ForeignKey(UserLists, on_delete=models.CASCADE)

    def __str__(self):
        return f"these are this users {self.name} analytics"
    
    def to_dict(self):
        return{
            'name': self.name,
            'user': self.user,
            'userlist': self.userlist
        }
    
    
class Comment(models.Model):
    rating = models.IntegerField()
    comments = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"this is a comment: {self.comments} . and this is a rating: {self.rating}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comments': self.comments,
            'user': self.user,
            'drink': self.drink
        }

class Achievements(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"this is {self.name} achievement"
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'user': self.user
        }

# will use this if we want to create a distiller admin 
# class Distiller(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     email = models.CharField(max_length=64) 
#     password = models.CharField(max_length=64) 
#     location = models.CharField(max_length=64)
#     # has many drinks
#     # has one analytic

#     def __str__(self):
#         return f"{self.name} is in {self.location}"

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.first_name,
#             # 'email': self.email,
#             # 'password': self.password,
#             'location': self.location
#         }