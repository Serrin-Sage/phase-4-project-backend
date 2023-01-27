from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User, UserLists, Analytics, Drink, Comment, Achievements
from django.views.decorators.csrf import csrf_exempt, csrf_protect

#DRINK VIEWS#

def drinks_id(request, id):
	try:
		drink = Drink.objects.get(id=id)
		return JsonResponse(drink.to_dict(), safe=False, status=201)
	except Drink.DoesNotExist:
		return JsonResponse({'error': 'Drink not found'})

def drinks_category(request, alcohol_type):
	try:
		drink = list(Drink.objects.filter(alcohol_type=alcohol_type).values())
		return JsonResponse(drink, safe=False, status=201)
	except Drink.DoesNotExist:
		return JsonResponse({'error': 'Drink Category not found'}), 404
	
def drinks_all(request):
	drinks = list(Drink.objects.values())
	return JsonResponse(drinks, safe=False, status=201)

#USER VIEWS#

def index_user(request):
	users = list(User.objects.values())
	return JsonResponse(users, safe=False, status=201)
 
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = list(User.objects.filter(
            username=data["username"], password=data["password"]).values())
        if user:
            return JsonResponse(user[0], safe=False)
        else:
            return JsonResponse({'Error': 'User not found'}, status=404)
    else:
        return JsonResponse({'Error': 'Invalid request method'})

def show_user(request, id):
	try:
		user = User.objects.get(id=id)
		return JsonResponse(user.to_dict(), safe=False, status=200)
	except User.DoesNotExist:
		return JsonResponse({'error': 'User not found'})
	
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User(first_name=data["first_name"], last_name=data['last_name'], username=data['username'],
                    email=data['email'], password=data['password'], age=data['age'], location=data['location'])
        # Why and how TF does this work!
        print(user)
        user.save()
        return JsonResponse({'success': True}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def update_user(request, id):
	if request.method == "PATCH": 
		user = User.objects.get(id=id)
		data = json.loads(request.body)
		for key, value in data.items():
			setattr(user, key, value)
		user.save()
		return JsonResponse({'success': True}, status=200)
	else:
		return JsonResponse({'error': 'Could not update'}, status=400)
	
def delete_user(request, id):
	try:
		user = User.objects.get(id=id)
	except User.DoesNotExist:
		return JsonResponse({'error': 'Could not find the user you are looking for'}, status=404)
	user.delete()
	return JsonResponse({'success': 'User has been deleted'}, status=200)

#LIST VIEWS#

def create_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        userlists = UserLists(name=data["name"], user_id=data['user_id'])
        # Why and how TF does this work!
        print(userlists)
        userlists.save()
        return JsonResponse({'success': True}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def index_lists(request):
	try:
		userlists = list(UserLists.objects.values())
		return JsonResponse(userlists, safe=False, status=201)
	except UserLists.DoesNotExist:
		return JsonResponse({'error': 'Lists do not exist'}, status=404)

def show_list(request, id):
	try:
		userlist = UserLists.objects.get(id=id)
		return JsonResponse(userlist.to_dict(), safe=False, status=200)
	except UserLists.DoesNotExist:
		return JsonResponse({'error': 'List not found'}, status=404)

def update_list(request, user_id, drink_id):
	if request.method == "PATCH":
		userlist = UserLists.objects.get(id=user_id)
		drink = Drink.objects.get(id=drink_id)
		# print (kwargs, type(kwargs))
		data = json.loads(request.body)
		userlist.drinks.add(drink)
		# for key, value in data.items():
		# 	setattr(userlist, key, value)
		userlist.save()
		return JsonResponse({'success': True}, status=200 )
	else:
		return JsonResponse({'error': 'Could not update'}, status=400)

def delete_list(request, id):
	try:
		userlists = UserLists.objects.get(id=id)
	except UserLists.DoesNotExist:
		return JsonResponse({'error': 'Could not find the list you are looking for'}, status=404)
	userlists.delete()
	return JsonResponse({'success': 'List has been deleted'}, status=200)

#Achievement Views#

def show_achievement(request, id):
	try:
		achievement = Achievements.objects.get(id=id)
		return JsonResponse(achievement.to_dict(), safe=False, status=200)
	except Achievements.DoesNotExist:
		return JsonResponse({'error': 'Achievement does not exist yet'}, status=404)
	
def update_achievement(request, id):
	if request.method == "PATCH":
		achievement = Achievements.objects.get(id=id)
		data = json.loads(request.body)
		for key, value in data.items():
			setattr(achievement, key, value)
		achievement.save()
		return JsonResponse({'success': True}, status=200)
	else:
		return JsonResponse({'error': 'Achievement not found'}, status=404)

#Analytics Views#

def create_analytic(request):
		if request.method == "POST":
			data = json.loads(request.body)
			analytic = Analytics(name=data["name"], user=data['user'])
			analytic.objects.create()
			analytic.save()
			return JsonResponse({'success': True}, status=200)
		else:
			return JsonResponse({'error': 'Invalid anayltic request method'}, status=400)

def update_analytic(request, id):
	if request.method == "PATCH":
		analytic = Analytics.objects.get(id=id)
		data = json.loads(request.body)
		for key, value in data.items():
			setattr(analytic, key, value)
		analytic.save()
		return JsonResponse({'success': True}, status=201)
	else:
		return JsonResponse({'error': 'Could not update the analytics'}, status=400)
	
#Comments Views#

def create_comment(request):
		if request.method == "POST":
			data = json.loads(request.body)
			comment = Comment(rating=data["rating"], comments=data["comments"], drink_id=data["drink_id"], user_id=data["user_id"])
			comment.save()
			return JsonResponse(comment.to_dict(), safe=False)
		else:
			return JsonResponse({'error': 'Could not generate the comment'})
		
def show_comments(request, id):
	try:
		comments = Comment.objects.get(id=id)
		return JsonResponse(comments.to_dict(), safe=False, status=200)
	except Comment.DoesNotExist:
		return JsonResponse({'error': 'Achievement does not exist yet'}, status=404)
	
def update_comment(request, id):
	if request.method == "PATCH":
		comment = Comment.objects.get(id=id)
		data = json.loads(request.body)
		for key, value in data.items():
			setattr(comment, key, value)
		comment.save()
		return JsonResponse({'success': True}, status=201)
	else:
		return JsonResponse({'error': 'Could not update the comment'}, status=400)

def delete_comment(request, id):
	try:
		comment = Comment.objects.get(id=id)
	except Comment.DoesNotExist:
		return JsonResponse({'error': 'Could not find the comment you are looking for'}, status=404)
	comment.delete()
	return JsonResponse({'success': 'Comment has been deleted'}, status=200)
