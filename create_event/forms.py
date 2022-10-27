from django.forms import ModelForm
from create_event.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['namaEvent', 'namaPantai', 'alamatPantai', 'jumlahPartisipan', 'fotoPantai', 'deskripsi', 'tanggalMulai', 'tanggalAkhir']
