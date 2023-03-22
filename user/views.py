from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# JSON
import json
from django.http import JsonResponse
#Model
from user.models import User

# Create your views here.
@csrf_exempt
def add(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("Post API Called",body['username'])
    newUser = User(
        username= body['username'],
        email= body['email'],
        password = body['password'],
        current_chapter = body['currentChapter']
    )
    newUser.save()
    del body['password']
    return JsonResponse({
        'status': 200,
        'message': "New manga successfully added.",
        'added': body,
        })

@csrf_exempt
def login(request): 
    body_unicode = request.body.decode('utf-8')   
    body = json.loads(body_unicode)   
    print("Login API Called",body['username'])   
    try:
        user = User.objects.filter(username__exact=body['username']).values()[0]
        if user['password'] == body['password']:
            user.pop('password')
            return JsonResponse({
                "status": {
                    "code": 200,
                    "message": "Login Success."
                },
                "data": user
            }, safe=False)
    except:
        return JsonResponse({
                "status": {
                    "code": 404,
                    "message": "Invalid Username or Password."
                },
                "data": {}
            }, safe=False)