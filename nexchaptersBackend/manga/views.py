from django.shortcuts import render
# Return JSON File
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({
        "mangaList": [
            {
            'title': 'one piece',
            'image': "https://static.wikia.nocookie.net/onepiece/images/c/c6/Volume_100.png/revision/latest?cb=20210903160940",
            'totalChapters': 1065,
            'currentChapter': 0,
            },{
                'title': 'one piece',
                'image': "https://static.wikia.nocookie.net/onepiece/images/c/c6/Volume_100.png/revision/latest?cb=20210903160940",
                'totalChapters': 1065,
                'currentChapter': 0,
            }
        ]})