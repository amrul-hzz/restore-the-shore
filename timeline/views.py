

from django.shortcuts import render
from create_event.models import Event
from django.shortcuts import redirect
from my_account.models import UserAccount
from django.db.models import F
from timeline.forms import sortForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/landing_page/login/')
def show_data(request):
   

    data_event = Event.objects.all()
    response = {
        'datalist':  data_event,
 
    }  

    if request.method == 'POST':
        form = sortForm()(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('timeline.html'))
    else:
        form = sortForm()
        response = {
        'datalist':  data_event,
        'form': form,
        }   
        return render(request, 'timeline.html', response)
    
    return render(request, "timeline.html", response)



def join_event(request):
    nama = request.POST['nama']
    event = Event.objects.filter(namaEvent=nama)
    print(event)
    
    
    