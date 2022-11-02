from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from create_event.models import *
from create_event.forms import *
from create_event.urls import *
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class CreateEventTestCase(TestCase):

    def test_show_create_event(self):
        self.client.user = User.objects.create_superuser('test', 'test@test.com', 'testpassword')
        self.client.login(username='test', password='testpassword')
        response = self.client.get('/create-event/')
        self.assertEqual(response.status_code, 200)

    def test_show_json(self):
        response = self.client.get(reverse('create_event:show_json'))
        self.assertEquals(response.status_code, 200)