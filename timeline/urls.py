from django.urls import path
from timeline.views import *

app_name = "timeline"

urlpatterns = [
    path('', show_data, name="show_data"),
    path('delete/<int:pk>/', delete_card, name='delete_card'),
]