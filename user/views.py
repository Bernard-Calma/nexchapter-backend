from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# JSON
import json
from django.http import JsonResponse, HttpResponse
#Model
from user.models import User
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login
# bcrypt
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
hasher = BCryptSHA256PasswordHasher()
import bcrypt


# Create your views here.
@csrf_exempt
def register(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("Register API Called",body['username'])
    request_user = { 
        "username": body['username'],
        "email": body['email'],
        "password": body['password'], 
    }
    if request_user['password'] != body['verifyPassword'] :
        error_message = "passwords does not match"
    try:
        request_user['password'] = request_user['password'].encode('utf-8')
        request_user['password'] = bcrypt.hashpw(request_user['password'], bcrypt.gensalt())
        new_user = User(
            username= request_user['username'],
            email= request_user['email'],
            password = request_user['password'],) 
        new_user.save()
        user_dict = model_to_dict(new_user)
        del user_dict['password']
        return JsonResponse({
             "status": {
                    "code": 200,
                    "message": "Registered Successfully."
                },
            'data': user_dict, 
            })
    except Exception as e:
        error_message = str(e) 
        print(error_message) 
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
    body_unicode = request.body.decode('utf-8')   
    body = json.loads(body_unicode)   
    print("Login API Called",body['username']) 
    try:
        user = User.objects.get(username__exact=body['username'])  
        user_dict = model_to_dict(user)
        if user_dict['password'] == body['password']:
            del user_dict['password']
            return JsonResponse({
                "status": { 
                    "code": 200,
                    "message": "Login Success."
                },
                "data": user_dict
            }, safe=False)
    except Exception as e:
        print("Error Loggin In: ", str(e)) 
        error_message = "Invalid username or password" 
        if body['username'] == "" or  body['password'] == "":
            error_message = "All fields should not be empty"
        return JsonResponse({
                "status": {
                    "code": 404,
                    "message": error_message
                },
                "data": {}
            }, safe=False)