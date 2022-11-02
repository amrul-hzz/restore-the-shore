from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class StatusTest(TestCase):
    def test_show_forum(self):
        client = Client()
        response = client.get(reverse('forum:show_forum'))

        self.assertEqual(response.status_code, 200)

    def test_show_forum_json(self):
        client = Client()
        response = client.get(reverse('forum:show_forum_json'))

        self.assertEqual(response.status_code, 200)

    def test_show_forum_json_by_user(self):
        client = Client()
        response = client.get(reverse('forum:show_forum_json_by_user'))

        self.assertEqual(response.status_code, 200)

    def test_show_comments_json(self):
        client = Client()
        response = client.get(reverse('forum:show_comments_json'))

        self.assertEqual(response.status_code, 200)

    def test_add_post(self):
        client = Client()
        response = client.get(reverse('forum:add_post'))

        self.assertEqual(response.status_code, 200)

    def test_add_comment(self):
        client = Client()
        response  = client.get(reverse('forum:add_comment'))

        self.assertEqual(response.status_code, 200)