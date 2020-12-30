from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    BookListView,
    BookDetailView,
    AddCommentView,
    about,
    fiction
)
from blog.models import Book

class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse('blog-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BookListView)

    def test_book_url_is_resolved(self):
        url = reverse('book-detail',Book.objects.get(pk=1))
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BookDetailView)

    def test_fiction_url_is_resolved(self):
        url = reverse('blog-fiction')
        print(resolve(url))
        self.assertEquals(resolve(url).func, fiction)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)