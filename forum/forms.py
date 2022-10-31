from django.forms import ModelForm
from forum.models import Post
from forum.models import Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
