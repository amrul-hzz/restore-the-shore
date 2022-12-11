from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import update_session_auth_hash
from landing_page.models import UserAccount
from timeline.models import JoinEvent
from .forms import ChangePasswordForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='landing_page:login_user')
def show_account(request):  
    data_user = UserAccount.objects.get(user = request.user)
    for event in JoinEvent.objects.filter(user = request.user):
        data_user.events_joined.add(event)
        data_user.save()
    data_user.user_point = data_user.events_joined.count() * 10
    context = {
        'user_data' : data_user,
    }
    return render(request, 'my_account.html', context)

@login_required(login_url='landing_page:login_user')
def show_json(request):
    data_user = UserAccount.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")

def password_change(request):
    form = ChangePasswordForm(user=request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("my_account:my_account")
    
    return render(request, 'password_change.html', {'form':form})

@csrf_exempt
def changePassword(request):
    form = ChangePasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return JsonResponse({"status" : "success", "message" : "berhasil"})
    return JsonResponse({"status" : "failed", "message" : "gagal"})

    

