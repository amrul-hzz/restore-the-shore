from django.urls import path
from leaderboard.views import show_leaderboard, show_json, search, add_quote
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('json/', show_json, name='show_json'),
    path('search/<str:searchusername>/', search, name='search'),
    path('add-quote/<str:quote>/', add_quote, name='add_quote'),
]