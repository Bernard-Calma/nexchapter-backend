from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Return JSON File
from django.core import serializers
import json
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.

# Model
from manga.models import Manga
def index(request):
    data = list(Manga.objects.values())
    return JsonResponse({'mangaList': data}, safe=False)

@csrf_exempt
def add(request):
    print("Post API Called")
    newManga = Manga(
        title= request.body.title,
        link = request.body.link,
        image= request.body.image,
        current_chapter = request.body.currentChapter
    )
    newManga.save()
    return JsonResponse({
        'status': 200,
        'message': "New manga successfully added.",
        'added': newManga,
        })
    # data = json.loads(request.body) 
    # print(data)
    # return HttpResponse(data['message']) 