from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from forum.views import show_forum
from forum.views import show_forum_json 
from forum.views import show_forum_json_by_user
from forum.views import show_comments_json
from forum.views import add_post
from forum.views import add_comment
from forum.views import post_post

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('json/', show_forum_json, name='show_forum_json'),
    path('json-by-user', show_forum_json_by_user, name='show_forum_json_by_user'),
    path('json-comments/<int:id>/', show_comments_json, name='show_comments_json'),
    path('add-post/', add_post, name='add_post'),
    path('add-comment/<int:id>/', add_comment, name='add_comment'),
    path('post-post-api/', post_post, name='post_post'),
]
