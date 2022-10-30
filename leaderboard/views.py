from django.shortcuts import render
from landing_page.models import UserAccount
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from leaderboard.models import LeaderBoard
from leaderboard.forms import AccountForm
from django.views.decorators.csrf import csrf_exempt
    
# Create your views here.
def show_leaderboard(request):
    data_leaderboard = User.objects.all() # Tambahkan berdasarkan jumlah join_event dari UserAccount
    paginator = Paginator(data_leaderboard, 1) # Show 5 account per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "leaderboards": data_leaderboard,
        "page_obj": page_obj,
    }
    return render(request, "leaderboard.html", context)

@csrf_exempt
def search(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'leaderboard.html', 'context')

def show_json(request):
    if request.method == "GET":
        data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
        return HttpResponse(serializers.serialize("json", data_leaderboard), content_type="application/json")
