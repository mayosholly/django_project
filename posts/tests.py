from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import PostListCreateView


class HelloWorld(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('posts_home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"],"Hello World")


class PostListCreateTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view=PostListCreateView.as_view()
        self.url=reverse("posts_list")

    def test_list_posts(self):
        request = self.factory.get(self.url)
        response=self.view(request)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation(self):
        pass