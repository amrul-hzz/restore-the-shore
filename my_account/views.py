from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from my_account.models import UserAccount

# Create your views here.
#@login_required(login_url='landing_page:login')
def show_account(request):  
    context = {
        #'user_data' : UserAccount.objects.filter(user = request.user)
    }
    return render(request, 'my_account.html', context)

# def show_achievments(request):

# def show_event_history(request):