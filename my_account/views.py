from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='landing_page:login')
def show_account(request):
    return render(request, 'my_account.html')

# def show_achievments(request):

# def show_event_history(request):