import json
from django.shortcuts import render
from landing_page.models import UserAccount
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from leaderboard.models import LeaderBoard
from leaderboard.forms import AccountForm
from django.views.decorators.csrf import csrf_exempt
from .models import LeaderBoard
import random
from django.contrib.auth.decorators import login_required
    
# Create your views here.
def show_leaderboard(request):
    data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
    paginator = Paginator(data_leaderboard, 2) # Show 2 account per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "leaderboards": data_leaderboard,
        "page_obj": page_obj,
    }
    return render(request, "leaderboard.html", context)

@csrf_exempt
def search(request, searchusername):
    if request.method == "GET":
        users = UserAccount.objects.filter(user__username__icontains=searchusername) # cari berdasarkan pola
        return HttpResponse(serializers.serialize("json", users), content_type="application/json")

@login_required(login_url="/welcome/login/")
@csrf_exempt
def add_quote(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False) # not yet saved to db
            user_acc = UserAccount.objects.get(user=request.user)
            form.users = user_acc
            form.save() # saved to db, by default your own made models
            return HttpResponse("OK")

    elif request.method == "GET":
        data_quote = list(LeaderBoard.objects.all())
        random_quote = random.choice(data_quote)

        context = {
            'random_quote': random_quote.quote,
            'name': random_quote.users.username
        }

        return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def get_quote(request):
    if request.method == "GET":
        data_quote = list(LeaderBoard.objects.all())
        random_quote = random.choice(data_quote)

        context = {
            'random_quote': random_quote.quote,
            'name': random_quote.users.username
        }

        return HttpResponse(json.dumps(context), content_type="application/json")

def show_json(request):
    if request.method == "GET":
        data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
        return HttpResponse(serializers.serialize("json", data_leaderboard), content_type="application/json")
