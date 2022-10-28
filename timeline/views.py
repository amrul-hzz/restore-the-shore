from django.shortcuts import render
from create_event.models import Event
from django.shortcuts import redirect
# Create your views here.

def show_data(request):
    print(Event.objects.all())
    data_event = Event.objects.all()
    response = {
        'datalist':  data_event,
 
    }  
    
    return render(request, "timeline.html", response)

def delete_card(request, pk):
    Event.objects.get(id=pk).delete()
    return redirect('timeline:show_data')

