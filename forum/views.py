from forum.models import Post, Comment
from .forms import PostForm, CommentForm

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import datetime

# Create your views here.
def show_forum(request):
    posts_data = Post.objects.all()
    context = {
        'posts_data' : posts_data
    }
    return render(request, "forum.html", context)

def show_forum_json(request):
    posts_data = Post.objects.all()
    return HttpResponse(serializers.serialize("json", posts_data), content_type="application/json")

@login_required(login_url="/landing_page/login_user/")
@csrf_exempt
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.date = datetime.datetime.now()
            form.save()

            return JsonResponse({
                "pk": form.pk,
                "fields":
                {
                    "creator": form.creator,
                    "date": form.date,
                    "content": form.content,
                    "image": form.image
                }
            });

@login_required(login_url="/landing_page/login_user/")
@csrf_exempt
def add_comment(request, id):
    if request.method == "POST":

        creator = request.user
        date = datetime.datetime.now()
        content = request.POST.get("content")
        original_post = Post.objects.get(pk=id)

        new_comment = Comment(creator=creator, date=date, content=content, original_post=original_post)
        new_comment.save()

        return JsonResponse({
            "pk": new_comment.pk,
            "fields":
            {
                "user": new_comment.creator.username,
                "date": new_comment.date,
                "content": new_comment.content,
                "original_post": id
            }
        })