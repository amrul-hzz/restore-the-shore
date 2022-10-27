from django.shortcuts import render
from create_event.models import Event
# Create your views here.

def show_data(request):
    
    data_event = Event().objects.all()
    response = {
        'datalist':  data_event,
 
    }  
    
    return render(request, "timeline.html", response)

def delete_card(request, pk):
    UMKM.objects.get(id=pk).delete()
    return redirect('timeline:show_data')