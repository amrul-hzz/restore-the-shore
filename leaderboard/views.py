from django.shortcuts import render
from my_account.models import UserAccount
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator

# TODO: import app dari fadlan

# Create your views here.
def show_leaderboard(request):
    data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user__date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
    paginator = Paginator(data_leaderboard, 25) # Show 25 account per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "leaderboards": data_leaderboard,
        "page_obj": page_obj,
    }
    return render(request, "leaderboard.html", context)

def show_json(request):
    if request.method == "GET":
        data_leaderboard = UserAccount.objects.all().order_by('-user_point', '-user.date_joined') # Tambahkan berdasarkan jumlah join_event dari UserAccount
        return HttpResponse(serializers.serialize("json", data_leaderboard), content_type="application/json")
