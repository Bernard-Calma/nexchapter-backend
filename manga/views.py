from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Return JSON File
import json
from django.http import JsonResponse
# Create your views here.

# Model
from manga.models import Manga
def index(request, id):
    data = list(Manga.objects.filter(user_id = id).values())
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

@csrf_exempt
def update(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body['image']) 
    manga_to_edit = Manga.objects.get(id=body['id'])
    manga_to_edit.title = body['title']
    manga_to_edit.image= body['image']
    manga_to_edit.link = body['link']
    manga_to_edit.current_chapter = body['current_chapter']
    manga_to_edit.save()
    return JsonResponse({
        'status': 200,
        'message': "Manga edited successfully.",
        'manga id': body['id'],
        })


@csrf_exempt
def delete(request, id):
    print("Delete route called")
    manga_to_delete = Manga.objects.get(id=id)
    manga_to_delete.delete()
    return JsonResponse({
        'status': 200,
        'message': "Manga Deleted successfully.",
        'manga id': id,
    })