from django.urls import path
from timeline.views import *

app_name = "timeline"

urlpatterns = [
    path('', show_data, name="show_data"),
   
    path('join-event/<str:nama>', join_event, name='join_event')
]