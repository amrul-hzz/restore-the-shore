from django.urls import path
from my_account.views import *

app_name = 'my_account'

urlpatterns = [
    path('', show_account, name='my_account'),
    
]
