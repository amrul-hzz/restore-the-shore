from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from create_event.models import Event
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from create_event.forms import EventForm

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def show_create_event(request):
    return render(request, "create_event.html")

@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def add_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
    user = request.user
    namaEvent = request.POST.get("namaEvent")
    namaPantai = request.POST.get("namaPantai")
    alamatPantai = request.POST.get("alamatPantai")
    jumlahPartisipan = request.POST.get("jumlahPartisipan")
    fotoPantai = request.POST.get("fotoPantai")
    deskripsi = request.POST.get("deskripsi")
    tanggalMulai = request.POST.get("tanggalMulai")
    tanggalAkhir = request.POST.get("tanggalAkhir")
    new_event = Event(
        user = user, 
        namaEvent = namaEvent,
        namaPantai = namaPantai,
        alamatPantai = alamatPantai,
        jumlahPartisipan = jumlahPartisipan,
        fotoPantai = fotoPantai,
        deskripsi = deskripsi,
        tanggalMulai = tanggalMulai,
        tanggalAkhir = tanggalAkhir,
    )
    return JsonResponse({
        "pk" : new_event.pk, "fields": {
        "namaEvent" : new_event.namaEvent,
        "namaPantai" : new_event.namaPantai,
        "alamatPantai" : new_event.alamatPantai,
        "jumlahPartisipan" : new_event.jumlahPartisipan,
        "fotoPantai" : new_event.fotoPantai,
        "deskripsi" : new_event.deskripsi,
        "tanggalMulai" : new_event.tanggalMulai,
        "tanggalAkhir" : new_event.tanggalAkhir,
    }})

@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def delete_event(request, id):
    data_delete = Event.objects.get(pk = id)
    data_delete.delete()
    return redirect("create_event:show_create_event")

def show_json(request):
    data_event = Event.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('create_event:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("create_event:show_create_event")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('create_event:login_user'))
    response.delete_cookie('last_login')
    return response