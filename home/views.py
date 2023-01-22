from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Example

# Create your views here.
def index(request): #gets all data from Example
	data = list(Example.objects.values())
	return JsonResponse(data, safe=False)