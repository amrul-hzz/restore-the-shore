from django.shortcuts import render, redirect
#from landing_page.models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    #if request.user.is_authenticated:
    #    if not UserAccount.objects.filter(user = request.user).exists(): # check if account already exist
    #        UserAccount.objects.create(user = request.user, user_point = 0)
    #context = {
    #    'this_user' : UserAccount.objects.filter(user = request.user)
    #    'last_login': request.COOKIES['last_login'],
    #}
    return render(request, "welcome.html")

#ini bener gasih buat nyimpen ke database?
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('landing_page:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            #response = HttpResponseRedirect(reverse("landing_page:welcome")) # membuat response
            #response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return redirect('landing_page:welcome')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    #response = HttpResponseRedirect(reverse('landing_page:login_user'))
    #response.delete_cookie('last_login')
    return redirect('landing_page:welcome')