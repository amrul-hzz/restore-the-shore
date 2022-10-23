from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from my_account.models import UserAccount
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
#@login_required(login_url='landing_page:login')
def show_account(request):  
    data_user = UserAccount.objects.filter(user = request.user)
    context = {
        'user_data' : data_user,
        'events_joined' : data_user.events_joined.all(),
    }
    return render(request, 'my_account.html', context)

def show_json(request):
    data_user = UserAccount.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")

# def show_achievments(request):

# def show_event_history(request):