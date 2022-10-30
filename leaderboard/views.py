from django.shortcuts import render
from landing_page.models import UserAccount
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from leaderboard.models import LeaderBoard
from leaderboard.forms import AccountForm
from django.views.decorators.csrf import csrf_exempt
from .models import LeaderBoard
import random
    
# Create your views here.
def show_leaderboard(request):
    data_leaderboard = LeaderBoard.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
    paginator = Paginator(data_leaderboard.user, 2) # Show 2 account per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "leaderboards": data_leaderboard,
        "page_obj": page_obj,
    }
    return render(request, "leaderboard.html", context)

# @csrf_exempt
# def search(request):
#     form = AccountForm()
#     if request.method == "POST":
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'leaderboard.html', context)

@csrf_exempt
def search(request, searchusername):
    if request.method == "GET":
        users = UserAccount.objects.filter(user__username__icontains=searchusername) # cari berdasarkan pola
        return HttpResponse(serializers.serialize("json", users), content_type="application/json")


def add_quote(request, quote):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False) # not yet saved to db
            form.user = request.user
            form.save() # saved to db, by default your own made models

            data_quote = list(LeaderBoard.objects.all())
            random_quote = random.choice(data_quote)

            context = {
                'random_quote': random_quote,
                'name': form.user.username
            }
            return context
            # return JsonResponse({
            #     "pk": form.pk,
            #     "fields": {
            #         "quote": form.quote,
            #         "name": form.user.username
            #     }
            # })

        

def show_json(request):
    if request.method == "GET":
        data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
        return HttpResponse(serializers.serialize("json", data_leaderboard), content_type="application/json")
