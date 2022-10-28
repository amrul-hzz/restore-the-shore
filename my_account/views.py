from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from landing_page.models import UserAccount

# Create your views here.
@login_required(login_url='landing_page:login_user')
def show_account(request):  
    # setiap register buat juga object UserAccount caranya UserAccount.objects.create(user = ..., user_point = 0)
    # Tiap join event tambahin events_joined caranya UserAccount.objects.get(user = request.user).events_joined.add(Event) kayaknya
    data_user = UserAccount.objects.get(user = request.user)
    context = {
        'user_data' : data_user,
        'events_joined' : data_user.events_joined.all(),
    }
    return render(request, 'my_account.html', context)

def show_json(request):
    data_user = UserAccount.objects.get(user = request.user)
    return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")