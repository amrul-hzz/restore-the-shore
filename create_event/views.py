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
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def show_create_event(request):
    return render(request, "create_event.html")

@csrf_exempt
def add_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return JsonResponse({
                "model" : "create_event.event",
                "pk" : form.pk, "fields": {
                "user" : form.user.pk,
                "namaEvent" : form.namaEvent,
                "namaPantai" : form.namaPantai,
                "alamatPantai" : form.alamatPantai,
                "jumlahPartisipan" : form.jumlahPartisipan,
                "fotoPantai" : form.fotoPantai,
                "deskripsi" : form.deskripsi,
                "tanggalMulai" : form.tanggalMulai,
                "tanggalAkhir" : form.tanggalAkhir,
            }})

@csrf_exempt
def add_event_mobile(request):
    username = request.POST.get('username')
    user = User.objects.get(username = username)
    nama_event = request.POST.get('namaEvent')
    nama_pantai = request.POST.get('namaPantai')
    alamat_pantai = request.POST.get('alamatPantai')
    jumlah_partisipan = request.POST.get('jumlahPartisipan')
    foto_pantai = request.POST.get('fotoPantai')
    deskripsi = request.POST.get('deskripsi')
    tanggal_mulai = request.POST.get('tanggalMulai')
    tanggal_akhir = request.POST.get('tanggalAkhir')
    tanggal_mulai_fix = datetime.strptime(tanggal_mulai, '%Y-%m-%d').date()
    tanggal_akhir_fix = datetime.strptime(tanggal_akhir, '%Y-%m-%d').date()

    new_event = Event.objects.create(
        user = user, 
        namaEvent = nama_event, 
        namaPantai = nama_pantai, 
        alamatPantai = alamat_pantai, 
        jumlahPartisipan = int(jumlah_partisipan), 
        fotoPantai = foto_pantai, 
        deskripsi = deskripsi, 
        tanggalMulai = tanggal_mulai_fix, 
        tanggalAkhir = tanggal_akhir_fix)
    new_event.save()
    return JsonResponse({
        "model" : "create_event.event",
        "pk" : 1, "fields": {
        "user" : user.pk,
        "namaEvent" : nama_event,
        "namaPantai" : nama_pantai,
        "alamatPantai" : alamat_pantai,
        "jumlahPartisipan" : jumlah_partisipan,
        "fotoPantai" : foto_pantai,
        "deskripsi" : deskripsi,
        "tanggalMulai" : tanggal_mulai_fix,
        "tanggalAkhir" : tanggal_akhir_fix,
    }})

@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def delete_event(request, id):
    data_delete = Event.objects.get(pk = id)
    data_delete.delete()
    return redirect("create_event:show_create_event")

@user_passes_test(lambda u: u.is_superuser)
def show_more_info(request, id):
    data_info = Event.objects.get(pk = id)
    context = {
        'info' : data_info,
    }
    return render(request, "show_info.html", context)

def show_json(request):
    data_event = Event.objects.all()
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")