from django.shortcuts import render
# Return JSON File
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

# Model
from manga.models import Manga
def index(request):
    return JsonResponse({
        "mangaList": [
            {
            'title': 'one piece',
            'image': "https://www.manga33.com/d/c2/one-piece.jpg",
            'totalChapters': 1065,
            'currentChapter': 0,
            },{
                'title': 'naruto',
                'image': "https://www.manga33.com/d/cover/iq5itsc1gsl.jpg",
                'totalChapters': 900,
                'currentChapter': 0,
            }
        ]})