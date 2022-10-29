from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from forum.views import show_forum
from forum.views import show_forum_json 
from forum.views import add_post
from forum.views import add_comment

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('json/', show_forum_json, name='show_forum_json'),
    path('add-post/', add_post, name='add_post'),
    path('add-comment/<int:id>/', add_comment, name='add_comment'),
]
