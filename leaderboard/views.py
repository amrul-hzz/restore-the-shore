from django.shortcuts import render
from my_account.models import UserAccount

# TODO: import app dari fadlan

# Create your views here.
def show_leaderboard(request):
    data_leaderboard = UserAccount.object.all()
    context = {
        "leaderboards": data_leaderboard
    }
    return render(request, "leaderboard.html", context)

# def show_json(request):

