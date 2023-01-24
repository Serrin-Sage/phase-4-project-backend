from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User, UserLists, Analytics, Drink, Comment, Achievements

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



