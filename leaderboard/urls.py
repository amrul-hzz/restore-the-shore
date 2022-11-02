from django.urls import path
from leaderboard.views import show_leaderboard, show_json, search, add_quote, get_quote
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('json/', show_json, name='show_json'),
    path('search/<str:searchusername>/', search, name='search'),
    path('add-quote/', add_quote, name='add_quote'),
    path('get-quote/', get_quote, name='get_quote'),
    # path('getuser/<int:id>/', get_user, name='get_user'),
]