from django.urls import path
from landing_page.views import logout_user, register, login_user, welcome, feedback, show_json

app_name = 'landing_page'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('json/', show_json, name='show_json'),
    path('feedback/', feedback, name='feedback')
]