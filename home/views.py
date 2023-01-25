from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User, UserLists, Analytics, Drink, Comment, Achievements
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
# def index(request): #gets all data from Example
# 	data = list(User.objects.values())
# 	return JsonResponse(data, safe=False)

def drinks_id(request, id):
	try:
		drink = Drink.objects.get(id=id)
		return JsonResponse(drink.to_dict(), safe=False, status=201)
	except Drink.DoesNotExist:
		return JsonResponse({'error': 'Drink not found'})

def drinks_category(request, alcohol_type):
	try:
		drink = list(Drink.objects.filter(alcohol_type=alcohol_type).values())
		return JsonResponse(drink, safe=False)
	except Drink.DoesNotExist:
		return JsonResponse({'error': 'Drink Category not found'}), 404
	
def drinks_all(request):
	drinks = list(Drink.objects.values())
	return JsonResponse(drinks, safe=False)

# @csrf_exempt
# def create_user(request):
# 	user_data = request.data
# 	user = User.objects.create_user(
		# first_name= user_data['first_name'],
		# last_name=user_data['last_name'],
		# username=user_data['username'],
		# email=user_data['email'],
		# password=user_data['password'],
		# age= user_data['age'],
		# location=user_data['location']
# 	)
# 	user.save()
# 	return JsonResponse(user, safe=False)




def index_user(request):
	users = list(User.objects.values())
	return JsonResponse(users, safe=False)


def show_user(request, id):
	try:
		user = User.objects.get(id=id)
		return JsonResponse(user.to_dict(), safe=False, status=201)
	except User.DoesNotExist:
		return JsonResponse({'error': 'User not found'})

	
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User(first_name=data["first_name"], last_name=data['last_name'], username=data['username'],
                    email=data['email'], password=data['password'], age=data['age'], location=data['location'])
        # Why and how TF does this work!
        print(user)
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

@csrf_exempt
def update_user(request, id):
	if request.method == "PATCH": 
		data = json.loads(request.body)
		user = User(first_name=data["first_name"])
		print(user)
		user.save()
		return JsonResponse({'success': True})
	else:
		return JsonResponse({'error': 'Could not update'})
