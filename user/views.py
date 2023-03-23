from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# JSON
import json
from django.http import JsonResponse, HttpResponse
#Model
from user.models import User

# Create your views here.
@csrf_exempt
def register(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("Register API Called",body['username'])
    requestUser = {
        "username": body['username'],
        "email": body['email'],
        "password": body['password'],
        "verify_password": body['verifyPassword']
    }

    if requestUser['password'] != requestUser['verify_password']:
        error_message = "passwords does not match"
    try:
        newUser = User(
            username= body['username'],
            email= body['email'],
            password = body['password'],
        )
        newUser.save()
        del body['password']
        return JsonResponse({
            'status': 200,
            'message': "New manga successfully added.",
            'added': body, 
            })
    except Exception as e:
        error_message = str(e) 
        email_check = error_message.find("email") == -1
        username_check = error_message.find("username") == -1
        if not email_check:
            error_message = "email already exist."
        elif not username_check:
            error_message = "username already exist."
        return JsonResponse({
            "status": {
                    "code": 404,
                    "message": error_message
                },
            }) 

@csrf_exempt
def login(request): 
    print(request.body) 
    body_unicode = request.body.decode('utf-8')   
    body = json.loads(body_unicode)   
    username = body['username']
    password = body['password']
    print("Login API Called",body['username'])
    try:
        user = User.objects.filter(username__exact=body['username']).values()[0]
        print("User: " , user)
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
        error_message = "Invalid username or password" 
        if username == "" or  password == "":
            error_message = "All fields should not be empty"
        return JsonResponse({
                "status": {
                    "code": 404,
                    "message": error_message
                },
                "data": {}
            }, safe=False)