from django.shortcuts import render
# Return JSON File
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

# Model
from manga.models import Manga
def index(request):
    data = list(Manga.objects.values())
    return JsonResponse({'mangaList': data}, safe=False)