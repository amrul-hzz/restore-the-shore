from django.urls import path
from create_event.views import show_create_event
from create_event.views import add_event
from create_event.views import show_json, login_user, register, logout_user, delete_event, show_more_info

app_name = "create_event"

urlpatterns = [
    path('show/', show_create_event, name="show_create_event"),
    path('add/', add_event, name="add_event"),
    path('json/', show_json, name = 'show_json'),
    path('delete-event/<int:id>/', delete_event, name = 'delete_event'),
    path('show-info/<int:id>/', show_more_info, name = 'show_info'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login_user'),
    path('logout/', logout_user, name = 'logout_user'),
]