from django.forms import ModelForm
from landing_page.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']