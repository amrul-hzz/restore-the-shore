from django import forms

SORT = [
    ('tanggal', 'Tanggal'),
    ('lokasi', 'Lokasi'),
    ('event', 'Event')

]

class sortForm(forms.Form):
    sort_choice = forms.Select(choices=SORT)