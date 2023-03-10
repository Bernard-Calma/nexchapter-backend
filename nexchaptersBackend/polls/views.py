from django.shortcuts import render
# Return JSON File
from django.http import JsonResponse
# Create your views here.
import json

def index(request):
    return JsonResponse({'foo': 'bar'})
    