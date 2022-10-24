from django.urls import path
from leaderboard.views import show_leaderboard, show_json

app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard, name='show_leaderboard'),
    path('json/', show_json, name='show_json'),
]