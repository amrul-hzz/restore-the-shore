from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from landing_page.models import UserAccount

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            if user.is_superuser:
                type = "admin",
            else:
                type = "user",
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            # Insert any extra data if you want to pass data to Flutter
            "username" : user.username,
            "type" : type,            
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if (User.objects.filter(username=username)):
            return JsonResponse({
                "status": False,
                "message": "The username has already been registered!"
                }, status=401)
        elif (password == repeat_password):
            user = User.objects.create_user(username = username, password = password)
            new_user_profile = UserAccount.objects.create(user=user, username = username)
            user.save()
            new_user_profile.save()
            return JsonResponse({
                "status": True,
                "message": "Successfully Create Account!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Password and repeat password are not the same!"
            }, status=401)

@csrf_exempt
def logout(request):
	if request.user.is_authenticated:
		auth_logout(request)
		return JsonResponse({"status" : False, "message" : "Successfully Logged Out!"}, status=200)
	return JsonResponse({"status": "Not yet authenticated", "message": "Failed to Logout"}, status =403)
