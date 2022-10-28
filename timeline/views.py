

from django.shortcuts import render
from create_event.models import Event
from django.shortcuts import redirect
from my_account.models import UserAccount
from django.db.models import F
from timeline.forms import sortForm
# Create your views here.

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

def delete_card(request, pk):
    Event.objects.get(id=pk).delete()

    return redirect('timeline:show_data')

def join_event(request):
    thisUser = UserAccount.objects.filter(user=request.user)
    thisUser.update(user_point==F('user_point') + 1)
    
    