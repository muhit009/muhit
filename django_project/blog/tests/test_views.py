from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Book,Comment
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('blog-home')
        self.book_url = reverse('book-detail')

    def test_book_list_view_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_book_book_detail_GET(self):
        response = self.client.get(self.book_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/book_detail.html')