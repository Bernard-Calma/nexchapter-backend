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
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("Post API Called",body['title'])
    newManga = Manga(
        title= body['title'],
        image= body['image'],
        link = body['link'],
        current_chapter = body['currentChapter']
    )
    newManga.save()
    return JsonResponse({
        'status': 200,
        'message': "New manga successfully added.",
        'added': body,
        })
