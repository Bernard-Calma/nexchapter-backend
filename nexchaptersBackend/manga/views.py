from django.shortcuts import render
# Return JSON File
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({
        'title': 'one piece',
        'image': "http://wwww.",
        'totalChapters': 1065,
        'currentChapter': 0,
    })