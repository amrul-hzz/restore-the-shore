from django.forms import ModelForm
from timeline.models import JoinEvent

class JoinEventForm(ModelForm):
    class Meta:
        model = JoinEvent
        fields = ['namaEvent', 'namaPantai', 'alamatPantai', 'jumlahPartisipan', 'fotoPantai', 'deskripsi', 'tanggalMulai', 'tanggalAkhir']
