from django.urls import path
from create_event.views import show_create_event
from create_event.views import add_event
from create_event.views import show_json, login_user, register, logout_user, delete_event

app_name = "create_event"

urlpatterns = [
    path('show/', show_create_event, name="show_create_event"),
    path('add/', add_event, name="add_event"),
    path('json/', show_json, name = 'show_json'),
    path('delete-event/<int:id>/', delete_event, name = 'delete_event'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login_user'),
    path('logout/', logout_user, name = 'logout_user'),
]