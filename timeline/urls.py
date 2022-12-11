from django.urls import path
from timeline.views import *

app_name = "timeline"

urlpatterns = [
    path('', show_data, name="show_data"),
   
    path('join-event/<str:nama>', join_event, name='join_event'),
    path('event_detail/<int:pk>/', show_event_by_id, name='show_event_by_id'),
    path('joinevent/', join_event, name='join_event'),
    path('json/', show_json, name = 'show_json'),
    path('json-all/', show_json_all, name = 'show_json_all(request)'),
    path('join-flutter/', join_flutter, name='join_flutter'),

]