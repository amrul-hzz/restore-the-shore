from django.urls import path
from create_event.views import show_create_event
from create_event.views import add_event
from create_event.views import show_json

app_name = "create_event"

urlpatterns = [
    path('show/', show_create_event, name="show_create_event"),
    path('add/', add_event, name="add_event"),
    path('json/', show_json, name = 'show_json'),
]