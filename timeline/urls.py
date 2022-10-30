from django.urls import path
from timeline.views import *

app_name = "timeline"

urlpatterns = [
    path('', show_data, name="show_data"),
   
    path('join-event/<str:nama>', join_event, name='join_event'),
    path('event_detail/<int:pk>/', show_event_by_id, name='show_event_by_id'),
    path('join_event/', join_event, name='join_event'),
    path('json/', show_json, name = 'show_json'),
]