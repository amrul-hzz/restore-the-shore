from django.urls import path
from landing_page.views import register, login, logout

app_name = 'landing_page'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]