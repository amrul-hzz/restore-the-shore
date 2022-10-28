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

@login_required(login_url="/create-event/login/")
@csrf_exempt
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.date = datetime.date.today()
            form.save()
    
    return JsonResponse(form) # not so sure about this
    
@login_required(login_url="/create-event/login/")
@csrf_exempt
def add_comment(request, id):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.creator = request.user
            form.date = datetime.date.today()
            form.original_post = Post.objects.all().filter(pk=id)
            form.save()

    return JsonResponse(form) # not so sure about this
