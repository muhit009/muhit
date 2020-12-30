from django.test import TestCase
from blog.models import Book, Comment

class TestModels(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            title='The Kite Runner',
            content='Good',
            date_posted=(2018, 7, 29, 12, 0, 13, 204815),
            author='khaled hossaini',
            genre='Fiction'
        )

    def test_book_creation(self):
        self.assertEquals(self.book1, Book.objects.all().first())