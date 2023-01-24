from django.contrib import admin
from .models import User, UserLists, Analytics, Drink, Comment, Achievements

# Register your models here.
admin.site.register(User)
admin.site.register(UserLists)
admin.site.register(Analytics)
admin.site.register(Drink)
admin.site.register(Comment)
admin.site.register(Achievements)
