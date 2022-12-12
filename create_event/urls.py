from django.urls import path
from create_event.views import show_create_event
from create_event.views import add_event
from create_event.views import show_json, delete_event, show_more_info, add_event_mobile

app_name = "create_event"

urlpatterns = [
    path('', show_create_event, name="show_create_event"),
    path('add/', add_event, name="add_event"),
    path('add-mobile/', add_event_mobile, name="add_event_mobile"),
    path('json/', show_json, name = 'show_json'),
    path('delete-event/<int:id>/', delete_event, name = 'delete_event'),
    path('show-info/<int:id>/', show_more_info, name = 'show_info'),
]