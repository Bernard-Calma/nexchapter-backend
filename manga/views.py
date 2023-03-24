from django.views.decorators.csrf import csrf_exempt
# Return JSON File
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
# Create your views here.

# Model
from manga.models import Manga
from user.models import User
def index(request, id):
    data = list(Manga.objects.filter(user_id = id).values())
    return JsonResponse({'mangaList': data}, safe=False)

@csrf_exempt
def add(request):
    body_unicode = request.body.decode('utf-8') 
    body = json.loads(body_unicode)
    print("Add Manga Route Called",body['title']) 
    user = User.objects.get(id=body['userID']) 
    new_manga = Manga(
        title= body['title'],
        image= body['image'],
        link = body['link'],
        current_chapter = body['currentChapter'], 
        user = user
    )
    new_manga.save()
    new_mangga_dict = model_to_dict(new_manga)
    print(f'User: {user} added {new_mangga_dict}')  
    return JsonResponse({
        'status': 200,
        'message': "New manga successfully added.",
        'added': new_mangga_dict,
        })

@csrf_exempt
def update(request, id): 
    print("Update route called")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode) 
    manga_to_edit = Manga.objects.get(id=id)
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